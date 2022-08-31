import pandas as pd
import names
import random
import datetime

from utils.generator import genrate_bc_id, genrate_postal_code, generate_bc_serial, genrate_phone_code, \
    genreate_cell_phone, generate_gender_fullname, generate_loan_info
from utils.database_operations import get_engine_pyodbc, generate_insert_customer_records, read_sql_file, \
    generate_insert_loan_records

n_data = 10000
n_loan = int(2.5 * n_data)

gender_fullname = [generate_gender_fullname() for _ in range(n_data)]
full_names, gender = zip(*gender_fullname)
customer_id = [random.randint(10000000, 99999999) for _ in range(n_data)]
branch_info = [(random.randint(1, 100000), names.get_last_name(), random.randint(100, 100000)) for _ in range(n_data)]
branch_id, branch, loan_superviser_id = zip(*branch_info)
birthdates = [datetime.date(random.randint(1900, 2022), random.randint(1, 12), random.randint(1, 28))
              for _ in range(n_data)]
fathers_name = [names.get_first_name(gender='male') for _ in range(n_data)]
bc_id = [genrate_bc_id(random.randint(1, 11)) for _ in range(n_data)]
bc_serial = [generate_bc_serial() for _ in range(n_data)]
postal_codes = [genrate_postal_code() for _ in range(n_data)]
phone_numbers = [genrate_phone_code() for _ in range(n_data)]
cell_phones = [genreate_cell_phone() for _ in range(n_data)]
nationality = list(random.choices([1, 0], weights=[0.9, 0.1], k=n_data))
bank_employee = list(random.choices([1, 0], weights=[0.05, 0.95], k=n_data))
military_service_status = list(random.choices([1, 0], weights=[0.6, 0.4], k=n_data))
customer_type = [random.randint(1, 10) for _ in range(n_data)]
is_alive = list(random.choices([1, 0], weights=[0.99, 0.01], k=n_data))
central_bank_status = [random.randint(1, 5) for _ in range(n_data)]

customer = pd.DataFrame(
    dict(full_name=full_names, customer_id=customer_id, branch_id=branch_id, branch=branch, birthdate=birthdates,
         father_name=fathers_name, bc_id=bc_id, bc_serial=bc_serial, gender=gender, iraninan_nationality=nationality,
         postal_code=postal_codes, phone_number=phone_numbers, cell_phone=cell_phones, bank_employee=bank_employee,
         military_service_status=military_service_status, customer_type=customer_type, is_alive=is_alive,
         central_bank_status=central_bank_status))

ix = customer.loc[customer.gender == 'female'].index
customer.loc[ix, 'military_service_status'] = 0
customer.drop_duplicates('customer_id', inplace=True)

loan_info = [generate_loan_info(customer.loc[random.choice(list(customer.index))]) for _ in range(n_loan)]
customer_id, deposit_id, deposit_type, deposit_balance, loan_balance, loan_id, wage, repayment_period, \
interest, repayment_method, penalty, guarantee_amount, loan_file_no, blocked_amount, \
guarantees_confirmation, loan_type = zip(*loan_info)

loan = pd.DataFrame(
    dict(customer_id=customer_id, deposit_id=deposit_id, deposit_type=deposit_type, deposit_balance=deposit_balance,
         loan_balance=loan_balance, wage=wage, repayment_period=repayment_period, interest=interest,
         repayment_method=repayment_method, penalty=penalty, guarantee_amount=guarantee_amount,
         loan_id=loan_id, loan_type=loan_type, loan_file_no=loan_file_no, blocked_amount=blocked_amount,
         guarantees_confirmation=guarantees_confirmation)
)

customer.drop_duplicates('customer_id', inplace=True)
conn = get_engine_pyodbc()
cursor = conn.cursor()

print('data created!')

# delete table if exist
query = read_sql_file('./utils/sql_queries/delete_table.sql')
cursor.execute(query)
conn.commit()

# create table
query = read_sql_file('utils/sql_queries/create_customer_table.sql')
cursor.execute(query)
conn.commit()

# insert to customer table
sql = read_sql_file('./utils/sql_queries/insert_customer_records.sql')
params = list(map(generate_insert_customer_records, [row for index, row in customer.iterrows()]))
cursor.executemany(sql, params)
cursor.commit()

print('insert customer record complete!')

# create table
query = read_sql_file('utils/sql_queries/create_loan_table.sql')
cursor.execute(query)
conn.commit()

# insert to customer table
sql = read_sql_file('./utils/sql_queries/insert_loan_records.sql')
params = list(map(generate_insert_loan_records, [row for index, row in loan.iterrows()]))
cursor.executemany(sql, params)
cursor.commit()
cursor.close()

print('insert loan record complete!')

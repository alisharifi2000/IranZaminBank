import pyodbc


def get_engine_pyodbc():
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=localhost;'
                          'Database=Bank;'
                          'UID=sa;'
                          'PWD=alisharifi1376119;'
                          'Trusted_Connection=yes;')
    return conn


def read_sql_file(path):
    sql_file = open(path, 'r')
    query = sql_file.read()
    query = query.replace('\n', " ")
    sql_file.close()
    return query


def generate_insert_customer_records(row):
    param = (row['full_name'],
             row['customer_id'],
             row['branch_id'],
             row['branch'],
             row['birthdate'].strftime('%Y-%m-%d'),
             row['father_name'],
             row['bc_id'],
             row['bc_serial'],
             row['gender'],
             row['iraninan_nationality'],
             row['postal_code'],
             row['phone_number'],
             row['cell_phone'],
             row['bank_employee'],
             row['military_service_status'],
             row['customer_type'],
             row['is_alive'],
             row['central_bank_status'])

    return param


def generate_insert_loan_records(row):
    param = (row['customer_id'],
             row['deposit_id'],
             row['loan_id'],
             row['loan_type'],
             row['deposit_type'],
             row['deposit_balance'],
             row['loan_balance'],
             row['wage'],
             row['repayment_period'],
             row['interest'],
             row['repayment_method'],
             row['penalty'],
             row['guarantee_amount'],
             row['loan_file_no'],
             row['blocked_amount'],
             row['guarantees_confirmation'])

    return param

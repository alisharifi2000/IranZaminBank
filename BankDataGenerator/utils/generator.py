import random
import string
import pandas as pd
import names


def generate_loan_info(customer):
    customer_id = customer['customer_id']
    branch_id = customer['branch_id']
    deposit_id = random.randint(100000000, 999999999)
    deposit_type = random.randint(1, 8)
    deposit_balance = random.uniform(-1000000000, 1000000000)
    loan_balance =random.uniform(0, 100000000)
    loan_id = genrate_loan_id()
    wage = loan_balance * 0.001
    repayment_period = random.choice([6, 12, 18, 24, 36, 60])
    repayment_method = random.choice([1, 2])
    interest = repayment_period * 0.5 * repayment_method * loan_balance / 100000000
    penalty = repayment_period * 0.001 * repayment_method
    guarantee_amount = loan_balance * 0.005 * repayment_method * repayment_period
    loan_type = random.randint(1, 10)
    loan_file_no = f'{branch_id}/{loan_type}-{loan_id}'
    guarantees_confirmation = random.choice([0, 1])
    blocked_amount = 0.05 * loan_balance

    return customer_id, deposit_id, deposit_type, deposit_balance, loan_balance, loan_id, \
           wage, repayment_period, interest, repayment_method, penalty, guarantee_amount, \
           loan_file_no, blocked_amount, guarantees_confirmation, loan_type


def genrate_bc_id(length):
    digits = [random.choice(string.digits) for _ in range(length)]
    bc_id = ''.join(digits)
    return bc_id


def genrate_loan_id():
    digits = [random.choice(string.digits) for _ in range(12)]
    loan_id = ''.join(digits)
    return loan_id


def generate_gender_fullname():
    gender = random.choice(['male', 'female'])
    fullname = names.get_full_name(gender=gender)
    return fullname, gender


def generate_bc_serial():
    digit_part1 = [random.choice(string.digits) for _ in range(2)]
    letter_part = random.choice(string.ascii_lowercase)
    digit_part2 = [random.choice(string.digits) for _ in range(6)]
    digit_part1 = ''.join(digit_part1)
    digit_part2 = ''.join(digit_part2)
    code = f'{digit_part1}{letter_part}{digit_part2}'
    return code


def genrate_postal_code():
    digits = [random.choice(string.digits) for _ in range(10)]
    postal_code = ''.join(digits)
    return postal_code


def genrate_phone_code():
    ostan_phone_info = pd.read_excel('utils/data/ostan_code.xlsx')
    ostan_phone_info.dropna(inplace=True)
    ostan_codes = list(ostan_phone_info['کد استان'].apply(lambda x: str(int(x))).values)
    ostan_code = random.choice(ostan_codes)
    first_digit = random.choice(string.digits)
    other_digit = [random.choice(string.digits) for _ in range(6)]
    other_digit = ''.join(other_digit)
    phone = f'0{ostan_code}-{first_digit}{first_digit}{other_digit}'
    return phone


def genreate_cell_phone():
    other_digits = [random.choice(string.digits) for _ in range(9)]
    other_digits = ''.join(other_digits)
    cell_phone = f'09{other_digits}'
    return cell_phone

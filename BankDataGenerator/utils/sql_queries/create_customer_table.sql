CREATE TABLE customer (
    id int NOT NULL IDENTITY(1,1),
    full_name varchar(255),
    customer_id varchar(12) NOT NULL PRIMARY KEY,
    branch_id varchar(8),
    branch varchar(255),
    birthdate date,
    father_name varchar(255),
    bc_id varchar(15),
    bc_serial varchar(10),
    gender varchar(6),
    iraninan_nationality bit,
    postal_code varchar(20),
    phone_number varchar(12),
    cell_phone varchar(11),
    bank_employee bit,
    military_service_status bit,
    customer_type int,
    is_alive bit,
    central_bank_status int
);
CREATE TABLE IF NOT EXISTS brand (
    brand_id BIGINT PRIMARY KEY,
    brand_name VARCHAR(64)
);

CREATE TABLE IF NOT EXISTS office (
    office_id BIGINT PRIMARY KEY,
    office_name VARCHAR(32),
    street VARCHAR(64),
    city VARCHAR(32),
    state_name VARCHAR(32),
    zip_code BIGINT
);

CREATE TABLE IF NOT EXISTS customer (
    customer_id BIGINT PRIMARY KEY,
    first_name VARCHAR(32),
    last_name VARCHAR(32),
    city VARCHAR(32),
    state_name VARCHAR(32),
    zip_code BIGINT,
    phone_number INT,
    email VARCHAR(32),
    registration_date DATE
);

CREATE TABLE IF NOT EXISTS car (
    car_id BIGINT PRIMARY KEY,
    current_office_id BIGINT REFERENCES office(office_id),
    brand_id BIGINT REFERENCES brand(brand_id),
    car_name VARCHAR(32),
    car_type VARCHAR(32),
    color VARCHAR(32),
    model_name VARCHAR(32),
    model_year INT,
    registration_date DATE
);

CREATE TABLE IF NOT EXISTS rental (
    rental_id BIGINT PRIMARY KEY,
    customer_id BIGINT REFERENCES customer(customer_id),
    car_id BIGINT REFERENCES car(car_id),
    pickup_office_id BIGINT REFERENCES office(office_id),
    return_office_id BIGINT REFERENCES office(office_id),
    pickup_date TIMESTAMP,
    return_date TIMESTAMP,
    booked_date TIMESTAMP,
    amount INT
);
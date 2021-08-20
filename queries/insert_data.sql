COPY brand
FROM '/code/script/data/brand.csv' 
DELIMITER ',' 
CSV HEADER;

COPY office
FROM '/code/script/data/office.csv' 
DELIMITER ',' 
CSV HEADER;

COPY customer
FROM '/code/script/data/customer.csv' 
DELIMITER ',' 
CSV HEADER;

COPY car
FROM '/code/script/data/car.csv' 
DELIMITER ',' 
CSV HEADER;

COPY rental
FROM '/code/script/data/rental.csv' 
DELIMITER ',' 
CSV HEADER;
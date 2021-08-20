# Challenge | Car Rental
The challenge is to design a data model for a rental car service in Mexico. From this model, create an ETL process to generate a table containing most reserved cars and their rental average time.

## Usage
For runing this flow you just need [docker](https://docs.docker.com/get-docker/).

To build the container run:

```bash
docker-compose up --build -d
```

You can use the following command to run the entire flow:

```bash
docker exec -it {CONTAINER_ID} ./run_flow.sh
```
Or run the following and run the flow step by step:

```bash
docker exec -it {CONTAINER_ID} bash
```

## Flow description

The container runs on a PostgreSQL image. The shell script runs the flow as follows:

1. **Intialize database** Creates the schema and tables for the Car Rental Database based on the DDL in *create_rdb.sql*.
2. **Insert dummy data** Creates a small set of dummy data for testing porpuses trough a python script (*create_data.py*) and uploads them to the database.
3. **Run ETL V1** Creates a View (*create_view.sql*) with the requiered metrics.
4. **Run ETL V2** Executes a python script (*etl .py*) which consist of an ETL process that loads the needed data from the database, computes the metrics and uploads them to a new table in another schema.

## Data model description

The model suposes a system having different car types for different brands. Every car is described by a unique identifier (car_id), name, brand, model, year, type (sedan, SUV, etc) and the location where is currenlty available. The company may have several locations around the country, each location (office) has his identifier and an address (street, city, state, zip code). A customer is described by a unique identifier, name, address,email, and phone number. When customers rent a car they can it up at any location and return it to another (or the same) location; every rental generates a rental_id an amount of payment and information about the car, the pickup location, pickup date, return date and return location. This model is ilustrated on the following ERD:

![alt text](/images/erd.png)

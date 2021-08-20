#!/bin/bash
set -e

printf "%s\n" "#####################"
printf "%s\n" " Intialize database #"
printf "%s\n" "#####################"

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
DROP SCHEMA IF EXISTS car_rental_database CASCADE;
DROP SCHEMA IF EXISTS car_rental_metrics CASCADE;
CREATE SCHEMA car_rental_database;
CREATE SCHEMA car_rental_metrics;
SET search_path TO car_rental_database;
\i queries/create_rdb.sql
EOSQL

printf "%s\n" "######################################"
printf "%s\n" " Insert some dummy data for testing  #"
printf "%s\n" "######################################"

python3 script/create_data.py

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
SET search_path TO car_rental_database;
\i queries/insert_data.sql
EOSQL


printf "%s\n" "################################################"
printf "%s\n" " Let's 'run' the ETL as a View in the database #"
printf "%s\n" "################################################"

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
SET search_path TO car_rental_database;
\i queries/create_view.sql
SELECT * FROM metrics_view;
EOSQL

printf "%s\n" "#######################"
printf "%s\n" " Check the results... #"
printf "%s\n" "#######################"
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL

SET search_path TO car_rental_database;
SELECT * FROM metrics_view;
EOSQL


printf "%s\n" "#############################################"
printf "%s\n" " Now let's run the ETL with a python script #"
printf "%s\n" "#############################################"

python3 script/etl.py

printf "%s\n" "#######################"
printf "%s\n" " Check the results... #"
printf "%s\n" "#######################"

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
SET search_path TO car_rental_metrics;
SELECT * FROM metrics_table;
EOSQL

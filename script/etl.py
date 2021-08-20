import os
from sqlalchemy import create_engine
import pandas as pd

class etl():
    def __init__(self):
        user = os.environ["POSTGRES_USER"]
        pwd = os.environ["POSTGRES_PASSWORD"]
        db = os.environ["POSTGRES_DB"]
        host = "localhost"
        port = 5432
        self.engine_source = create_engine(
            f"postgresql+psycopg2://{user}:{pwd}@{host}:{port}/{db}",
            connect_args={
                'sslmode': 'prefer',
                'options': '-csearch_path=car_rental_database'
            },
            echo = False,
            encoding='utf8',
            pool_pre_ping = True)

        self.engine_target = create_engine(
            f"postgresql+psycopg2://{user}:{pwd}@{host}:{port}/{db}",
            connect_args={
                'sslmode': 'prefer',
                'options': '-csearch_path=car_rental_metrics'
            },
            echo = False,
            encoding='utf8',
            pool_pre_ping = True)

    def run(self):
        # Run the ETL process
        self._extract()
        self._transform()
        self._load()

    def _extract(self):
        # Extract the necessary tables for computing the required metrics 
        df_rentals = pd.read_sql_table(
            table_name="rental",
            con=self.engine_source)
        df_cars = pd.read_sql_table(
            table_name="car",
            con=self.engine_source)
        self.rentals = df_rentals
        self.cars = df_cars
        print("Data successfully obtained!")

    def _transform(self):
        # Compute the metrics: number of reservations and average rental time 
        df = pd.merge(
            left=self.rentals[["rental_id", "car_id", "pickup_date", "return_date"]],
            right=self.cars[["car_id", "car_name"]],
            how="left",
            on="car_id"
        )
        df["avg_rental_time"] = (df["return_date"] - df["pickup_date"]).dt.total_seconds() / 3600

        final_df = df[["rental_id", "car_id", "avg_rental_time"]].groupby(["car_id"], as_index=False)  \
                    .agg({"rental_id": "count", "avg_rental_time": "mean"})

        final_df.rename(columns={"rental_id": "reservations"}, inplace=True)
        self.final_df = final_df.sort_values(by=["reservations", "avg_rental_time"], ascending=False)
        print("Successfully computed the metrics!")

    def _load(self):
        # Upload the final metrics dataframe to a new table
        df = self.final_df
        df.to_sql(
            name="metrics_table", 
            con=self.engine_target,
            index=False,
            if_exists="replace")
        print("Successfully uploaded!")

if __name__ == "__main__":
    etl().run()


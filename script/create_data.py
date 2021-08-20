import pandas as pd
import random
import datetime

def create_data() :
    print("Creating dummy data...")
    df_office = pd.DataFrame(
        data={
            "office_id": list(range(1,6)),
            "office_name": [ f"office_{i}" for i in range(1,6)],
            "street": [ f"street_{i}" for i in range(1,6)],
            "city": ["city_{}".format(random.randint(1,4)) for i in range(1,6)],
            "state_name": ["state_{}".format(random.randint(1,3)) for i in range(1,6)],
            "zip_code": [random.randint(1,100) for i in range(1,6)],
        }
    )

    df_brand = pd.DataFrame(
        data={
            "brand_id": list(range(1,5)),
            "brand_name": ["Volkswagen", "Nissan", "Chevrolet", "Toyota"]
        }
    )
    car_brand = {
        "Jetta":1,
        "Tiguan":1,
        "Gol":1,
        "Sentra":2,
        "March":2,
        "Kicks":2,
        "Beat":3,
        "Cavalier":3,
        "Tracker":3,
        "Yaris":4,
        "Corolla":4,
        "Rav4":4
    }

    car_type = {
        "Jetta":"Sedan",
        "Tiguan":"SUV",
        "Gol":"Subcompacto",
        "Sentra":"Sedan",
        "March":"Subcompacto",
        "Kicks":"SUV",
        "Beat":"Chevrolet",
        "Cavalier":"Sedan",
        "Tracker":"SUV",
        "Yaris":"Subcompacto",
        "Corolla":"Sedan",
        "Rav4":"SUV"
    }

    rdn_cars = random.choices(list(car_brand.keys()), k=25)

    df_car = pd.DataFrame(
        data={
            "car_id": list(range(1,26)),
            "current_office_id": random.choices(list(range(1,6)), k=25),
            "brand_id": [ car_brand[i] for i in  rdn_cars],
            "car_name": rdn_cars,
            "car_type": [ car_type[i] for i in  rdn_cars],
            "color": random.choices(["azul", "negro", "blanco"], k=25),
            "model_name": ["base"]*25,
            "model_year": random.choices([2017,2018,2019], k=25),
            "registration_date": [datetime.date(year=2020, month=1, day=21)]*25
        }
    )

    df_customer = pd.DataFrame(
        data={
            "customer_id": list(range(1,36)),
            "firts_name": [ f"cliente_{i}" for i in range(1,36)],
            "last_name": [ f"apellido_{i}" for i in range(1,36)],
            "city": random.choices(list(range(1,4)), k=35),
            "state_name": random.choices(list(range(1,3)), k=35),
            "zip_code": random.choices(list(range(1,100)), k=35),
            "phone_number": random.choices(list(range(1,100)), k=35),
            "email": [ f"email_{i}" for i in range(1,36)],
            "registration_date": [datetime.date(year=2020, month=1, day=21)]*35
        }
    )

    aux_l = []
    counter = 1
    for car in list(range(1,26)) :
        res = random.randint(1,10)
        tmp_date = datetime.datetime(year=2020, month=random.randint(2,6), day=random.randint(1,28), hour=random.randint(8,22))
        for r in range(res) :
            aux_d = {}
            aux_d["rental_id"] = counter
            aux_d["customer_id"] = random.randint(1,35)
            aux_d["car_id"] = car
            aux_d["pickup_office_id"] = random.randint(1,5)
            aux_d["return_office_id"] = random.randint(1,5)
            aux_d["pickup_date"] = tmp_date
            tmp_date = tmp_date + datetime.timedelta(hours=random.randint(2,168))
            aux_d["return_date"] = tmp_date
            aux_d["booked_date"] = tmp_date - datetime.timedelta(days=1)
            delta = aux_d["return_date"] - aux_d["pickup_date"]
            aux_d["amount"] = int(delta.total_seconds() / 3600) * 100
            counter = counter + 1

            aux_l.append(aux_d)

    df_rental = pd.DataFrame.from_dict(aux_l)

    df_brand.to_csv("script/data/brand.csv", index=False)
    df_car.to_csv("script/data/car.csv", index=False)
    df_customer.to_csv("script/data/customer.csv", index=False)
    df_office.to_csv("script/data/office.csv", index=False)
    df_rental.to_csv("script/data/rental.csv", index=False)
    print("Dummy data created and saved!")

if __name__ == "__main__":
    create_data()
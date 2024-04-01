"""
This is a boilerplate pipeline 'visualize'
generated using Kedro 0.18.14
"""

import csv
from faker import Faker
import random
from datetime import datetime, timedelta
import os
import sqlite3
import pandas as pd


fake = Faker()

def generate_fake_data():
    date = fake.date_between(start_date='-365d', end_date='today')
    location = fake.city()
    min_temp = round(random.uniform(-10, 30), 1)
    max_temp = round(min_temp + random.uniform(0, 20), 1)
    rainfall = round(random.uniform(0, 10), 1)
    evaporation = "NA"
    sunshine = "NA"
    wind_gust_dir = fake.random_element(elements=('N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'))
    wind_gust_speed = random.randint(20, 60)
    wind_dir_9am = fake.random_element(elements=('N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'))
    wind_dir_3pm = fake.random_element(elements=('N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'))
    wind_speed_9am = random.randint(5, 20)
    wind_speed_3pm = random.randint(10, 25)
    humidity_9am = random.randint(50, 90)
    humidity_3pm = random.randint(30, 70)
    pressure_9am = round(random.uniform(1000, 1030), 1)
    pressure_3pm = round(random.uniform(990, 1020), 1)
    cloud_9am = random.randint(0, 9)
    cloud_3pm = random.randint(0, 9)
    temp_9am = round(random.uniform(min_temp, max_temp), 1)
    temp_3pm = round(random.uniform(min_temp, max_temp), 1)
    rain_today = fake.random_element(elements=('Yes', 'No'))
    rain_tomorrow = fake.random_element(elements=('Yes', 'No'))

    return [date, location, min_temp, max_temp, rainfall, evaporation, sunshine, wind_gust_dir, wind_gust_speed,
            wind_dir_9am, wind_dir_3pm, wind_speed_9am, wind_speed_3pm, humidity_9am, humidity_3pm, pressure_9am,
            pressure_3pm, cloud_9am, cloud_3pm, temp_9am, temp_3pm, rain_today, rain_tomorrow]


def save_data_to_db(num_rows: int, table_name: str):
    columns = ["Date", "Location", "MinTemp", "MaxTemp", "Rainfall", "Evaporation", "Sunshine", "WindGustDir",
               "WindGustSpeed", "WindDir9am", "WindDir3pm", "WindSpeed9am", "WindSpeed3pm", "Humidity9am",
               "Humidity3pm", "Pressure9am", "Pressure3pm", "Cloud9am", "Cloud3pm", "Temp9am", "Temp3pm",
               "RainToday", "RainTomorrow"]

    data = [generate_fake_data() for _ in range(num_rows)]
    df = pd.DataFrame(data, columns=columns)

    conn = sqlite3.connect("asi.db")
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()



def generate_fake_csv(file_path, num_rows):
    header = ["Date", "Location", "MinTemp", "MaxTemp", "Rainfall", "Evaporation", "Sunshine", "WindGustDir",
              "WindGustSpeed", "WindDir9am", "WindDir3pm", "WindSpeed9am", "WindSpeed3pm", "Humidity9am",
              "Humidity3pm", "Pressure9am", "Pressure3pm", "Cloud9am", "Cloud3pm", "Temp9am", "Temp3pm",
              "RainToday", "RainTomorrow"]
    
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)

        for _ in range(num_rows):
            fake_data = generate_fake_data()
            writer.writerow(fake_data)

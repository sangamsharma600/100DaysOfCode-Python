##################### Normal Starting Project ######################
import datetime as dt
import random 
import smtplib
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
MY_EMAIL = os.getenv('my_email')
MY_PASSWORD =os.getenv('password')


now = dt.datetime.now()
today_month = now.month
today_day = now.day

today_tuple = (today_month,today_day)

birthday_data = pd.read_csv("Day 30/birthdays.csv")

birthday_dict = {(data_row.month,data_row.day): data_row for (_, data_row) in birthday_data.iterrows()}
if (today_tuple) in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"Day 30/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]",birthday_person['name'])

    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=birthday_person['email'], msg=f"Subject: Happy Birthday\n\n{contents}")


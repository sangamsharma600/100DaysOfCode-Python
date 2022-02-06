import datetime as dt
import random
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

my_email = os.getenv('my_email')
password =os.getenv('password')

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 6:
     with open("Day 29/quotes.txt", encoding="utf-8") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)
        data=quote.encode(encoding='utf-8')
        decode_data=data.decode('utf-8')
        msg = MIMEText(decode_data)
        msg['Subject'] = 'Happy Sunday'
        msg['From'] = my_email
        receivers='sangamsharma600@gmail.com'
        
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(my_email, receivers, msg.as_string())
    
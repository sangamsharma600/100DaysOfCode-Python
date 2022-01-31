# import smtplib


# TODO: Use your own email and password #
my_email = "myemail@gmail.com"
password = "Password"
# # Securing Email Privacy #
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="sangamsharma600@gmail.com", msg="Subject:Hello There !!!\n\nHello there, this is a testing mail.")




# import datetime as dt

import datetime as dt
import random
import smtplib

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 6:
    with open("Day 29/quotes.txt", encoding="utf-8") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)
        print(quote)
    
    with smtplib.SMTP("smtp.gmail.com", 465) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, to_addrs='sangamsharma600@gmail.com', msg=f"Subject:Happy Sunday\n\n{quote.encode()}")

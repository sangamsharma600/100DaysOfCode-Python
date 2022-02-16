from smtplib import SMTP
import requests
import datetime as dt
import os
from dotenv import load_dotenv
import html
from email.mime.text import MIMEText

load_dotenv() 

MY_EMAIL = os.environ["my_email"]
PASSWORD = os.environ["password"]

FOREX_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

percent_diff = 0
now = dt.datetime.now()
today = now.today()
yesterday = today - dt.timedelta(days=1)
day_before_yesterday = yesterday - dt.timedelta(days=1)
yesterday = str(yesterday).split(" ")[0]
day_before_yesterday = str(day_before_yesterday).split(" ")[0]

title = []
body = []


fx_parameters = {
    "function": "DIGITAL_CURRENCY_DAILY",
    "symbol": "BTC",
    "market":"USD",
    "apikey":os.environ['stock_api']
}

# Getting News Articles #
def get_news():
    response = requests.get(NEWS_ENDPOINT,params=news_parameters)
    data = response.json()
    for i in range(3):
        title.append(data["articles"][i]["title"])
        body.append(data["articles"][i]["description"])

news_parameters = {
    "q": "bitcoin",
    "apiKey": os.environ["news_api"]
}

# Checking Rate Difference and Percentage Difference #
response = requests.get(FOREX_ENDPOINT,params=fx_parameters)
response.raise_for_status()
data = response.json()

closing_rate = float(data["Time Series (Digital Currency Daily)"][yesterday]["4b. close (USD)"])
previous_closing_rate = float(data["Time Series (Digital Currency Daily)"][day_before_yesterday]["4b. close (USD)"])
rate_difference = round(abs(closing_rate - previous_closing_rate),3)
percent_diff = round(abs((previous_closing_rate - closing_rate)/previous_closing_rate * 100),2)

if percent_diff > 0.2:
    get_news()


with SMTP("smtp.gmail.com",587) as connection:
    symbol = ''
    if closing_rate > previous_closing_rate:
        symbol = "UP"
    else:
        symbol = "DOWN"
    connection.starttls()
    connection.login(MY_EMAIL,PASSWORD)
    for i in range(3):
        body_content = html.unescape(body[i])
        title_content = html.unescape(title[i])
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL,msg=f"Subject:BITCOIN {symbol} by {percent_diff}%\n\nTitle: {title_content.encode()}")


 
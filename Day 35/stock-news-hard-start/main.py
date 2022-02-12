import requests
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv() 

FOREX_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

percent_diff= 0
now = dt.datetime.now()
today = now.today()
yesterday = today - dt.timedelta(days=1)
day_before_yesterday = yesterday - dt.timedelta(days=1)
yesterday = str(yesterday).split(" ")[0]
day_before_yesterday = str(day_before_yesterday).split(" ")[0]



fx_parameters = {
    "function": "DIGITAL_CURRENCY_DAILY",
    "symbol": "BTC",
    "market":"USD",
    "apikey":os.environ['stock_api']
}

# Getting News Articles #
def get_news():
    title = []
    body = []
    response = requests.get(NEWS_ENDPOINT,params=news_parameters)
    data = response.json()
    for i in range(3):
        title.append(data["articles"][i]["title"])
        body.append(data["articles"][i]["description"])
        print(f"\nALERT ⚠, The BTCUSD rate is differed by {percent_diff}%.\nTitle: {title[i]}.\nDescription: {body[i]}\n\n")

news_parameters = {
    "q": "bitcoin",
    "apiKey": os.environ["news_api"]
}

#  #
## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. '
response = requests.get(FOREX_ENDPOINT,params=fx_parameters)
response.raise_for_status()
data = response.json()

closing_rate = float(data["Time Series (Digital Currency Daily)"][yesterday]["4b. close (USD)"])
previous_closing_rate = float(data["Time Series (Digital Currency Daily)"][day_before_yesterday]["4b. close (USD)"])
rate_difference = round(abs(closing_rate - previous_closing_rate),3)
print(rate_difference)
percent_diff = round(abs((previous_closing_rate - closing_rate)/previous_closing_rate * 100),2)
print(percent_diff)
if percent_diff > 0.5:
    get_news()

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.


 
#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


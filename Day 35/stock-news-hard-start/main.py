import requests
import datetime as dt

FOREX_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

now = dt.datetime.now()
today = now.today()
yesterday = today - dt.timedelta(days=1)
day_before_yesterday = yesterday - dt.timedelta(days=1)
yesterday = str(yesterday).split(" ")[0]
day_before_yesterday = str(day_before_yesterday).split(" ")[0]


fx_parameters = {
    "function": "FX_DAILY",
    "from_symbol": "USD",
    "to_symbol":"NPR",
    "apikey":"MC2Q5LDPPY7ULHKR"
}


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. '
response = requests.get(FOREX_ENDPOINT,params=fx_parameters)
response.raise_for_status()
data = response.json()

closing_rate = float(data["Time Series FX (Daily)"][yesterday]["4. close"])
previous_closing_rate = float(data["Time Series FX (Daily)"][day_before_yesterday]["4. close"])
rate_difference = abs(closing_rate - previous_closing_rate)
rounded_diff = f"{rate_difference:.3f}"

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


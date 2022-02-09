from urllib import response
from dotenv import load_dotenv
import requests
from twilio.rest import Client
import os

load_dotenv()

account_sid = os.environ['account_sid']
auth_token = os.environ['auth_token']
api_key = os.environ['api_key']

MY_LAT='27.712021'
MY_LON='85.312950'
TWILIO_PHONE_NUMBER = os.environ['twilio_phone_number']
MY_PHONE_NUMBER = os.environ['my_phone_number']

parameters = {
    "lat": MY_LAT,
    "lon":MY_LON,
    "appid":api_key,
    "exclude":"current,daily,alerts,minutely"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall",params=parameters)
response.raise_for_status()

weather_data = response.json()

weather_data_slice = weather_data['hourly'][:12]

will_rain = False
for hour_data in weather_data_slice:
    weather_condition_id = hour_data['weather'][0]['id']
    if int(weather_condition_id)<700:
        will_rain = True

if will_rain:
    client = Client(account_sid,auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Don't forget to take an ☔.",
        from_= TWILIO_PHONE_NUMBER,
        to=MY_PHONE_NUMBER
    ),
    


import smtplib
import time
import requests
import datetime as dt
from dotenv import load_dotenv
import os

load_dotenv()
MY_EMAIL = os.getenv('my_email')
MY_PASSWORD =os.getenv('password')


MY_LAT = 27.9853627
MY_LON = 82.4159216
UTC_HOUR = 5
UTC_MINUTE = 45


now = dt.datetime.now()
hour_in_nepal = now.hour

def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()
    iss_latitude = float(data["iss_position"]['latitude'])
    iss_longitude = float(data["iss_position"]['longitude'])

    if abs(MY_LAT - iss_latitude) < 5 and abs(MY_LON - iss_longitude)<5:
        return True

def is_night():
    parameters = {
    'lat':MY_LAT,
    'lng':MY_LON,
    'formatted': 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = data['results']['sunrise']
    sunset = data['results']['sunset']

    nepal_hour_sunrise  =int(sunrise.split("T")[1].split(":")[0]) + UTC_HOUR
    nepal_minute_sunrise  =int(sunrise.split("T")[1].split(":")[1]) + UTC_MINUTE
    sunrise_nepal = (nepal_hour_sunrise*60)+(nepal_minute_sunrise)
    nepal_hour_sunrise =sunrise_nepal//60
    nepal_minute_sunrise = sunrise_nepal%60 

    nepal_hour_sunset  =int(sunset.split("T")[1].split(":")[0]) + UTC_HOUR
    nepal_minute_sunset  =int(sunset.split("T")[1].split(":")[1]) + UTC_MINUTE
    sunset_nepal = (nepal_hour_sunset*60)+(nepal_minute_sunset)
    nepal_hour_sunset = sunset_nepal//60
    nepal_minute_sunset = sunset_nepal%60 

    if nepal_hour_sunrise >= hour_in_nepal and nepal_hour_sunset <= hour_in_nepal:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead and is_night:
        connection = smtplib.SMTP("smtp.gmail.com",587)
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL,msg=f"Subject:Look Up\n\nThere is a iss sattellite over you. Go look Up.")
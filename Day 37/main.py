import requests
import os
from dotenv import load_dotenv
import datetime as dt

today_date= dt.datetime.now().strftime("%X")
now_time = dt.datetime.now().strftime("%d/%m/%Y")   

load_dotenv()

sheety_api_url = os.environ["SHEETY_API_URL"]
nutrition_api_endpoint = os.environ["NUTRITION_API_ENDPOINT"]

nutrition_api_endpoint_parameters = {
    'query':input("What did you did today ? : "),
}

sheety_api_post = {}

nutrition_api_headers = {
    "x-app-id":os.environ["NUTRITION_API_APPID"],
    "x-app-key":os.environ["NUTRITION_API_APPKEY"],
    "x-remote-user-id":"0"
}

response = requests.post(nutrition_api_endpoint,json=nutrition_api_endpoint_parameters,headers=nutrition_api_headers)
data = response.json()
exercise_data = data["exercises"]

for exercise in exercise_data:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    print(sheet_inputs)
    
    sheet_response = requests.post(sheety_api_url, json=sheet_inputs)
# print(user_input)
# print(duration_minutes)
# print(calories)


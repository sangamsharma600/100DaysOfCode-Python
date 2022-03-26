import os
from twilio.rest import Client
from dotenv import load_dotenv

number_list=["+9779809787080","+9779847899121"]

load_dotenv()
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['account_sid']
auth_token = os.environ['auth_token']
TWILIO_PHONE_NUMBER=os.environ['twilio_phone_number']

for number in number_list:
    client = Client(account_sid,auth_token)
    message = client.messages \
        .create(
        body="\nWishing you happiness, success and glory. May your Holi celebrations this year be memorable.\n\nSangam Sharma",
        from_= TWILIO_PHONE_NUMBER,
        to = number
    ),
    print(f"SMS Sent To {number}")
    
    

    
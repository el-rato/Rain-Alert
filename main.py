from dotenv import load_dotenv
load_dotenv()

import requests
from twilio.rest import Client
import os
OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
my_lat = 23.20
my_long = 77.0
params = {
    "lat": my_lat,
    "lon": my_long,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_endpoint,params=params)
response.raise_for_status()
weather_data = response.json()

is_rain = False
for hour_data in weather_data["list"]:
    weather_id = hour_data["weather"][0]["id"]

    if int(weather_id) < 700:
        is_rain = True
if is_rain == True:
    client = Client(account_sid, auth_token )
    message =  client.messages.create(
        
        body ="Its Raining 🐈 and 🐕",
        from_="twilio phone number",
        to= "intended Phone number"
    )
print(message.sid)
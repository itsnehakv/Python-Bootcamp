import requests
from dotenv import load_dotenv
load_dotenv()

# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
import json


account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
api_id = os.environ["OPENWEATHER_API_KEY"]

parameters={
    # "q":"Bengaluru,India",
    "lat":12.971599,
    "lon":77.594566,
    "appid":api_id
}
response=requests.get(f"https://api.openweathermap.org/data/2.5/forecast",params=parameters)
# f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LONG}&appid={weather_key}")
response.raise_for_status()
print(response.status_code)
data=response.json()
print(data)


will_it_rain=False
for hour in data["list"]:
    weather_id=hour["weather"][0]["id"]
    print(weather_id)
    if weather_id < 700:
        will_it_rain=True
if will_it_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_="whatsapp:+14155238886",
        to="whatsapp:+919538999279",
        body="Bring an umbrella ♡☂ "
    )
    print(message.status)
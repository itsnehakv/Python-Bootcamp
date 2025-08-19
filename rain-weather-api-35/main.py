import requests
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
import json

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid ="AC5384dcd299c8e1acc7365fe6ad4c5c43"
auth_token ="c67e4aaad4e2af3e3b8aa52ea1c81721"


api_id="a53b094fa13a1dd154d9e11dba0a9b39"
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
# print(data)


will_it_rain=False
for hour in data["list"]:
    weather_id=hour["weather"][0]["id"]
    # print(weather_id)
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

    # print("Bring an umbrella")

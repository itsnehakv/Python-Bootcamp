import requests
import os
from datetime import datetime

APP_ID="c894ba14"
API_KEY="d6f3127b9bda678213e471ad8de6abae"

WEIGHT=62
HEIGHT=155
AGE=19

URL="https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_input=input("How much did you exercise today?  ")

header={
    "x-app-id":os.environ["APP_ID"],
    "x-app-key":os.environ["API_KEY"]
}

exercise_params={
    "query": exercise_input,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

post_response=requests.post(url=URL,json=exercise_params,headers=header)
result=post_response.json()
print(result)
day=datetime.now()
day_format=day.strftime("%d/%m/%Y")
time_format=day.strftime("%H:%M:%S")
SHEET_URL=os.environ["SHEETY_ENDPOINT"]
BEARER_HEADER={
    "Authorization": f"Bearer {os.environ["BEARER_TOKEN"]}",
}

for exercise in result["exercises"]:
    sheet_inputs={
        "workout": {
            "date": day_format,
            "time": time_format,
            "exercise":exercise["name"].title(),
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"]
        }
    }

    sheet_post=requests.post(url=SHEET_URL,json=sheet_inputs,headers=BEARER_HEADER)
    print(sheet_post.text)




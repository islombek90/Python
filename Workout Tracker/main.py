import requests
from datetime import datetime
import os
os.environ['API_ID']="9b6868e5"
os.environ['API_KEY']="740b3b3124b768a50ca6e6a382eefa5b"
today_date = datetime.now()
time = today_date.strftime("%H:%M:%S")
date = today_date.strftime("%m/%d/%Y")

API_ID = os.environ.get('API_ID')

API_KEY = os.environ.get('API_KEY')

headers = {

    "x-app-id" : API_ID,
    "x-app-key" : API_KEY,

    "Content-Type": "application/json"


}


post_requests = {
 "query": input("which exercise you have finished: "),
 "gender":"male",
 "weight_kg":67.8,
 "height_cm":178,
 "age":31
}

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=post_requests, headers= headers)
docs_body = response.json()
print(docs_body)
print(len(docs_body["exercises"]))
docs_api_endpoint = "https://api.sheety.co/494752bacdc57c0b70812e7cdec9953d/myWorkouts/workouts"

google_docs_auth = {"Authorization":"Basic aXNsb21iZWs5MDpkZW1uMTJkZW1uMzQ"}
# requests.get(url=docs_api_endpoint,headers=google_docs_auth)

for exercise in range(0,len(docs_body["exercises"])):
    body = {
        "workout": {
            "date": date,
             "time" : time,
             "calories" : docs_body["exercises"][exercise]["nf_calories"],
             "duration" : docs_body["exercises"][exercise]["duration_min"],
             "exercise" : docs_body["exercises"][exercise]["user_input"].title()
        }
    }

requests.post(url=docs_api_endpoint, json=body, headers=google_docs_auth)


import requests
from datetime import datetime, timedelta
import json

today_date = datetime.now().strftime("%d/%m/%Y")
to_date = (datetime.now() + timedelta(90)).strftime("%d/%m/%Y")

print(today_date)
print(to_date)
flight_api_ednpoint = "https://tequila-api.kiwi.com/v2/flights_multi"
API_KEY = "3tvH-Pk2K1ry1hhIw-eSoHUZwb4RTbZZ"

headers = {"apikey" : API_KEY}


class FlightSearch:

  def flight_multicity_serach(self, city):

      body = {
        "requests": [
          {
            "fly_to": city,
            "fly_from": "IST",
            "dateFrom": today_date,
            "dateTo": to_date,
              "max_stopovers": "1",
              "curr": "USD",
          },

        ],
        "locale": "en",


      }

      response = requests.post(url=flight_api_ednpoint, json=body,headers=headers)
      with open("data.json", 'w')  as data_file:
        json.dump(response.json(), data_file)






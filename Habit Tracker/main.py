import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la//v1/users"

TOKEN  =  "asdasdasdasdasada"
USERNAME =  "islombek"
GRAPH_ID = "graph1"

user_params = {
    "token" : TOKEN,
    "username": USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"

}

# response = requests.post(url=pixela_endpoint, json=user_params)
# response.raise_for_status()
# print(response)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
print(graph_endpoint)

graph_config = {
    "id" : GRAPH_ID,
    "name" : "Cycling graph",
    "unit" : "km",
    "type" : "float",
    "color" : "kuro"

}

headers = {
    "X-USER-TOKEN" : TOKEN

}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

new_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
#selecting special date and formattıng as preferred
toda_date = datetime(year=2021, month=11, day = 12)

habit_edit = {
    "date" : toda_date.strftime("%Y%m%d"),
    "quantity" : "15.1"

}

response = requests.post(url=new_pixel_endpoint, json=habit_edit, headers=headers)
print(response.text)
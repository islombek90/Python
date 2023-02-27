import requests

docs_api_endpoint = "https://api.sheety.co/494752bacdc57c0b70812e7cdec9953d/flightDeals/prices"


google_docs_auth = {"Authorization":"Basic aXNsb21iZWs5MDpkZW1uMTJkZW1uMzQ"}

class DataManager:

    def get_required_fight(self):
        response = requests.get(url=docs_api_endpoint)
        response.raise_for_status()
        my_data =response.json()
        print(response)
        return my_data["prices"]

    # def update_iata_codes(self):
    #
    #     for exercise in range(0, len(docs_body["exercises"])):
    #         body = {
    #             "prices": {
    #                 "iataCode": date,
    #
    #             }
    #         }
    #
    #     requests.post(url=docs_api_endpoint, json=body, headers=google_docs_auth)








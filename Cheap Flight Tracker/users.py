import requests

users_doc_endpoint ="https://api.sheety.co/494752bacdc57c0b70812e7cdec9953d/flightDeals/flightClub"

google_docs_auth = {"Authorization":"Basic aXNsb21iZWs5MDpkZW1uMTJkZW1uMzQ"}

responses = requests.get(url=users_doc_endpoint)
print(responses.json())

class Users:
    def __init__(self):
        self.name = input("what is you name: ")
        self.surname = input("what is your surname: ")
        self.email = input("what is you email: ")
        self.email_confirmation = input("confirm your email: ")

    def new_users(self):
        body = {
            "flightClub": {
                "name": self.name.title(),
                 "surname" : self.surname.title(),
                 "mail" : self.email_confirmation

            }
        }
        if self.email == self.email_confirmation:

            requests.post(url=users_doc_endpoint, json=body)
            print("new user created succesfully")
        else:
            print("emails does not match, new acc not created ")



new_acc = Users()
new_acc.new_users()
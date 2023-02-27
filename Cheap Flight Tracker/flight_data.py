import json
from data_manager import DataManager
from notification_manager import NotificationManager

data = DataManager()
cities = data.get_required_fight()

class FlightData:
    def compare_price(self, city_price):
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            print(len(data[0]))
            for flights in range(0,len(data[0])):
                if data[0][flights]["price"] < city_price:
                    message= (f'cheap ticket found: {data[0][flights]["price"]} USD to {data[0][flights]["cityTo"]}\n{data[0][flights]["deep_link"]}\n{data[0][flights]["deep_link"]}')
                    send = NotificationManager()
                    # send.send_sms_notification(message)
                    send.send_mail_notification(message)
                    print(message)



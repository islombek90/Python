from twilio.rest import Client
import smtplib
import requests

account_sid = '' #twilio sid
auth_token = '' #twilio token

users_doc_endpoint ="https://api.sheety.co/494752bacdc57c0b70812e7cdec9953d/flightDeals/flightClub"
class NotificationManager:
    def send_sms_notification(self, message):
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            messaging_service_sid='', # twilio message sid
            body=message,
            to='' #enter your phone number
        )

        print(message.sid)
    def send_mail_notification(self,message):

        my_email = "" #enter you email
        password = "" #enter your password
        response = requests.get(url=users_doc_endpoint)
        data = response.json()


        for mails in range(0, len(data)):
            send_mails=data["flightClub"][mails]["mail"]
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()  # trasnport layer
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=send_mails,
                                        msg=f"Subject:Low Price Alert\n\n {message}")



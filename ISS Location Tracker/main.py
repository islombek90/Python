import requests
from datetime import datetime as dt
import smtplib
import time

counter = 0
run_the_program = True

def iss_location_mail_sender():

    MY_LAT =41.008240
    MY_LNG =28.978359

    EMAIL = "" #enter you mail here
    PASSWORD = "" #enter your password here

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()["iss_position"]
    latitude = float(data["latitude"])
    longitude = float(data["longitude"])
    print(latitude,longitude)
    # print(data)

    parameters = {
        "lat" : MY_LAT,
        "lng": MY_LNG,
        "formatted" : 0

    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters,)
    response.raise_for_status()
    data = response.json()["results"]
    # print(data)
    sunrise = int(data["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["sunset"].split("T")[1].split(":")[0])
    print(sunrise)
    print(sunset)

    time_now = dt.now()
    now = time_now.hour
    print(time_now.hour)

    if  MY_LAT -5 < latitude < MY_LAT +5 and   MY_LNG - 5 < longitude <  MY_LNG+5:
        if  now >= sunset or now <= sunrise :
            print(time_now)
            print("it is dark")
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=EMAIL, to_addrs="islombek90@gmail.com", msg="Subject: ISS HERE\n\n look up")
        else:
            print("it is dayligh you can not see")


while run_the_program:
    time.sleep(60)
    print("checking......")
    iss_location_mail_sender()

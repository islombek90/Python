import requests
import smtplib
from bs4 import BeautifulSoup
URL = "http://hepsiburada.com/lixada-dijital-projeksiyon-calar-saat-buyuk-led-ekran-calar-yurt-disindan-p-hbcv00000o8ws3"

r = requests.get(URL, headers = {"Accept-Language":"tr,en-US;q=0.9,en;q=0.8,uz;q=0.7,ru;q=0.6", "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"  }).text
soup = BeautifulSoup(r,"html.parser")

current_price = float(soup.find("span",class_="price" )["content"])
print(current_price)

EMAIL = ""  #enter you mail here
PASSWORD = "" #enter you password here

if current_price  < 350:

    print("price is down")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs="islombek90@gmail.com", msg=f"Subject: price down\n\n the new price is {current_price} check the link{URL}" )
else:
    print("waiting for discount")
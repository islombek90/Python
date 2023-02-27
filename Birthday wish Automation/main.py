##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
import random
import pandas as pd


now = dt.datetime.now()
day_of_week = now.day
month = now.month
today_date = (day_of_week,month)
print(today_date)
data_file = pd.read_csv("birthdays.csv")
#birthday_dict = {new_key:new_value for (index,row) in data_file.iterrow()}
birthday_dict = {(data_row["day"],data_row["month"]):data_row for (today_date,data_row) in data_file.iterrows()}
wish_letter = ["letter_1.txt","letter_2.txt","letter_2.txt"]
print(birthday_dict)

letter = random.choice(wish_letter)
if today_date in birthday_dict:
    print(today_date)
    birthday_person = birthday_dict[today_date]
    print("heyyy")

    with open(f"letter_templates/{letter}", "r") as selected_letter:
        modified_letter = selected_letter.read()
        modified_letter = modified_letter.replace("[NAME]", f"{birthday_person['name']}")
        print(modified_letter)
        print(birthday_person)
        print(birthday_person["email"])
#
#


    my_email = ""  # enter your mail
    password = "" # enter your password

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()   #trasnport layer
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday\n\n {modified_letter}")



##################### Extra Hard Starting Project ######################
import os
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")


import smtplib
import random
import datetime as dt
num = random.randint(1,3)


now = dt.datetime.now()
today = (now.month, now.day)
import  pandas
file = pandas.read_csv("birthdays.csv")
data = file.to_dict(orient="records")
dict_file = {key["name"]:{"email": key["email"], "birthday":( key["month"], key["day"])} for key in data}
for birth in dict_file:
    if today == dict_file[birth]["birthday"]:
        with open(f"letter_templates/letter_{num}.txt",mode= "r") as txt:
            text = txt.read()
            msg = text.replace("[NAME]",birth)
            print(msg)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=dict_file[birth]["email"], msg = f"Subject: Birthday \n\n {msg}")



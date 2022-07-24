import datetime as dt
import pandas
import smtplib

now=dt.datetime.now()
today=(now.month, now.day)
dic={}
df=pandas.read_csv("birthdays.csv")
dic={data["name"]:(data["month"], data["day"]) for (index,data) in df.iterrows()}

for (key,value) in dic.items():
    if value == today:
        print(key)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="gtest7402@gmail.com", password="atxrvgpysmiibiib")
            connection.sendmail(
                from_addr="gtest7402@gmail.com",
                to_addrs="singh.harjas2002@gmail.com",
                msg=f'Subject:Wish Birthday to {key}\n\nIts {key},s Birthday Today!!!!'
            )






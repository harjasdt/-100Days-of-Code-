import smtplib
import datetime as dt
import random


with open("quotes.txt") as file:
    list=file.readlines()

r_line=random.choice(list)

my_email="gtest7402@gmail.com"
my_pass="rangilakutta123"

now=dt.datetime.now()

if now.weekday()==4:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="gtest7402@gmail.com", password="atxrvgpysmiibiib")
        connection.sendmail(
            from_addr=my_email,
            to_addrs="singh.harjas2002@gmail.com",
            msg=f'Subject:Hello\n\n{r_line}'
        )



print(r_line)

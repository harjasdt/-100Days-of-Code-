import requests
from datetime import date
from datetime import timedelta
import smtplib
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_api_key="KW1C7DWMH9A8BT01"
news_api_key="e55bdd98b00a4672b9801731104f4456"

today = date.today()
t_1 = today - timedelta(days = 1)
t_2 = today - timedelta(days = 2)
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_parameters={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":stock_api_key
}
response=requests.get(url="https://www.alphavantage.co/query", params=stock_parameters).json()
data=response["Time Series (Daily)"]
d1=data[str(t_1)]["4. close"]
d2=data[str(t_2)]["4. close"]
diff=round(((float(d1)-float(d2))/float(d2))*100,4)


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news_prameters={
    "apiKey":news_api_key,
    "q":"tesla"
}
top_headlines = requests.get(url="https://newsapi.org/v2/top-headlines", params=news_prameters).json()
print(top_headlines['articles'][0])

if diff>5 or diff<-5:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="gtest7402@gmail.com", password="atxrvgpysmiibiib")
        connection.sendmail(
            from_addr="gtest7402@gmail.com",
            to_addrs="singh.harjas2002@gmail.com",
            msg=f"Subject:{top_headlines['articles'][0]['title']} \n\nNEWS:{top_headlines['articles'][0]['description']} \n\nURL:{top_headlines['articles'][0]['url']}"
        )





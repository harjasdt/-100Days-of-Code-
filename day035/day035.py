import requests
import os

api_endpoint="https://api.openweathermap.org/data/2.5/onecall"
parameters={
    "lat":22.303894,
    "lon": 70.802162,
    "appid":os.environ['keyy'],
    "exclude":"current,minutely,daily"
}

response=requests.get(url=api_endpoint,params=parameters).json()
we=[]
for i in range(0,13):
    x=response["hourly"][i]["weather"][0]["id"]
    we.append(x)
print(we)
if max(we)>700:
    print("raining")
else:
    print("cool")

we=[]
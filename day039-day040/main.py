#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from pprint import pprint
sheety_api="https://api.sheety.co/f94482e928c78729c2052c3d0c34b12c/sky/prices"
header={
    "Authorization": "Bearer hbfgjybthrvjrbt",
}
response=requests.get(url=sheety_api,headers=header).json()
sheet_data=response['prices']
pprint(sheet_data)
for i in sheet_data:
    if i["code"]=='':
        i["code"]="TESTING"
pprint(sheet_data)

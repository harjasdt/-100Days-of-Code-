import requests

sheety_api="https://api.sheety.co/f94482e928c78729c2052c3d0c34b12c/sky/prices"
header={
    "Authorization": "Bearer hbfgjybthrvjrbt",
}
response=requests.get(url=sheety_api,headers=header).json()
sheet_data=response['prices']

for i in sheet_data:
    new_api = f"https://api.sheety.co/f94482e928c78729c2052c3d0c34b12c/sky/prices/{i['id']}"
    if i["code"]=='':
        i["code"]="TESTING"
    sheetly_params = {
            "price": {
                "city":i['city'],
                "code":i["code"],
                "price":i["price"]
            }
        }
    done=requests.put(url=new_api,headers=header,json=sheetly_params)
    print(done.text)
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    pass

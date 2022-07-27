import requests
ll=31.147129
mm=75.341217
# response=requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.json())

parameters={
    "lat":ll,
    "lng":mm,
}
response=requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
# data=response.get()
# sunrise=data["results"]["sunrise"]
print(response.json())
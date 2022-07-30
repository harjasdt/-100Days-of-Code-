import requests
import datetime as dt

STRING=input("Log your activity: ")
api_id="a4526734"
api_key="4195af5a1a86fc0ea62c4d765afbf0e9"
api_endpoint="https://trackapi.nutritionix.com/v2/natural/exercise"
prams={
    "query":STRING,
    "gender":"female",
    "weight_kg":72.5,
    "height_cm":167.64,
    "age":30
}
header={
    "x-app-id":api_id,
    "x-app-key":api_key,

}

sheetly_header={
    "Authorization":"Bearer csrvdvbteadvbrav"
}
sheetly_endpoint="https://api.sheety.co/f94482e928c78729c2052c3d0c34b12c/sheet/workouts"

data=requests.post(url=api_endpoint,json=prams, headers=header).json()

# time and date
today=dt.datetime.now()
DATE=today.strftime("%m/%d/%Y")
TIME=today.strftime("%H:%M:%S")

for i in data["exercises"]:
    EXERCISE=i['name'].title()
    CALORIES = i['nf_calories']
    DURATION=i['duration_min']
    sheetly_params = {
        "workout": {
            "date": DATE,
            "time": TIME,
            "exercise": EXERCISE,
            "duration": f"{float(DURATION)}min",
            "calories": CALORIES,
        }
    }

    response = requests.post(url=sheetly_endpoint, json=sheetly_params, headers=sheetly_header)
    print(DURATION)






import requests

question_data=[]
parameter={
    "amount":"10",
    "type":"boolean",
}
response=requests.get(url="https://opentdb.com/api.php", params=parameter)
response.raise_for_status()


for i in range(0,10):
    question_data.append({"question":response.json()["results"][i]["question"], "correct_answer":response.json()["results"][i]["correct_answer"]})

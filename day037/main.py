import requests
import datetime as dt

#create user
USER="harjas"
TOKEN="abcdsedxcd123"
account_keypoint="https://pixe.la/v1/users"
account_params={
    "token":TOKEN,
    "username":USER,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
# response=requests.post(url=account_keypoint, json=account_params)
# print(response.text)
GRAPH_NAME="graph-id"
graph_keypoint=f"https://pixe.la/v1/users/{USER}/graphs"
graph_params={
    "id":GRAPH_NAME,
    "name":"coding graph",
    "unit":"day",
    "type":"int",
    "color":"sora",
}
graph_header={
    "X-USER-TOKEN":TOKEN,
}

# response=requests.post(url=graph_keypoint, json=graph_params, headers=graph_header)
# print(response.text)
today=dt.datetime.now().date().strftime("%Y%m%d")
add_keypoint=f"https://pixe.la/v1/users/{USER}/graphs/{GRAPH_NAME}"
add_params={
    "date":today,
    "quantity":"1",
}

header={
    "X-USER-TOKEN":TOKEN
}

# response=requests.post(url=add_keypoint, json=add_params, headers=header)
# print(response.text)

edit_keypoint=f"https://pixe.la/v1/users/{USER}/graphs/{GRAPH_NAME}/{today}"
edit_prams={
    "quantity":"0"
}
# response=requests.put(url=edit_keypoint, json=edit_prams, headers=header)
# print(response.text)

del_keypoint=f"https://pixe.la/v1/users/{USER}/graphs/{GRAPH_NAME}/{today}"
response=requests.delete(url=edit_keypoint, headers=header)
print(response.text)
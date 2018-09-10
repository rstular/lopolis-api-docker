import json

import requests

HOST = "http://localhost:5000/"

r = requests.post(HOST + "gettoken", data=json.dumps({"username": "<username>", "password": "<password>"}), headers={"Content-Type": "application/json"})

jsonData = json.dumps({"choices": {"2018-09-13T00:00:00.0000000": "29210", "2018-09-14T00:00:00.0000000": "38086"}})

data2 = requests.post(HOST + "setmenus", data=jsonData, headers={"Content-Type": "application/json", "Authorization": "Bearer " + json.loads(r.text)["data"]})

print(data2.text)

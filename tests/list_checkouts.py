#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

import requests

HOST = "https://lopolis-api.now.sh/"

r = requests.post(HOST + "gettoken", data=json.dumps({"username": "<username>", "password": "<password>"}), headers={"Content-Type": "application/json"})

jsonData = json.dumps({"year": "2018", "month": "9"})

data2 = requests.post(HOST + "getcheckouts", data=jsonData, headers={"Content-Type": "application/json", "Authorization": "Bearer " + json.loads(r.text)["data"]})

print(data2.text)

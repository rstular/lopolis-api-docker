#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

import requests

HOST = "http://localhost/"

r = requests.post(HOST + "gettoken", data=json.dumps({"username": "<username>", "password": "<password>"}), headers={"Content-Type": "application/json"})

jsonData = json.dumps({"choices": {"2018-09-24T00:00:00.0000000": "Malica", "2018-09-21T00:00:00.0000000": "Malica"}})

data2 = requests.post(HOST + "setcheckouts", data=jsonData, headers={"Content-Type": "application/json", "Authorization": "Bearer " + json.loads(r.text)["data"]})

print(data2.text)

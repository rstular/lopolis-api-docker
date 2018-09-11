import json

from flask import Flask, make_response, request

import api_lib
from helpers import About

app = Flask(__name__)

@app.route("/gettoken", methods=["POST"])
def gettoken():

    content = request.get_json()

    if len(content) == 2 and "username" in content and "password" in content:
        login_result = api_lib.GetToken(content["username"], content["password"])
        return json.dumps(login_result), login_result["status_code"]
    else:
        return "{\"error\": true, \"status_code\": 400}", 400

@app.route("/getmenus", methods=["POST"])
def getmenus():

    content = request.get_json()

    if len(content) == 2 and "year" in content and "month" in content and not request.headers.get("Authorization") is None:
        try:
            authorization_token = request.headers.get("Authorization").split("Bearer ")[1]
            if len(authorization_token) != 288:
                raise ValueError("Token not the right length")
        except:
           return "{\"error\": true, \"status_code\": 400}", 400 

        menus_result = api_lib.GetMenus(authorization_token, content["year"], content["month"])
        return json.dumps(menus_result), menus_result["status_code"]
    else:
        return "{\"error\": true, \"status_code\": 400}", 400

@app.route("/getcheckouts", methods=["POST"])
def getcheckouts():

    content = request.get_json()

    if len(content) == 2 and "year" in content and "month" in content and not request.headers.get("Authorization") is None:
        try:
            authorization_token = request.headers.get("Authorization").split("Bearer ")[1]
            if len(authorization_token) != 288:
                raise ValueError("Token not the right length")
        except:
           return "{\"error\": true, \"status_code\": 400}", 400 

        checkouts_result = api_lib.GetCheckouts(authorization_token, content["year"], content["month"])
        return json.dumps(checkouts_result), checkouts_result["status_code"]
    else:
        return "{\"error\": true, \"status_code\": 400}", 400

@app.route("/setmenus", methods=["POST"])
def setmenus():

    content = request.get_json()

    if len(content) == 1 and "choices" in content and not request.headers.get("Authorization") is None:
        try:
            authorization_token = request.headers.get("Authorization").split("Bearer ")[1]
            if len(authorization_token) != 288:
                raise ValueError("Token not the right length")
        except:
           return "{\"error\": true, \"status_code\": 400}", 400 
        
        menus_result = api_lib.SetMenus(authorization_token, content["choices"])
        return json.dumps(menus_result), menus_result["status_code"]

    else:
        return "{\"error\": true, \"status_code\": 400}", 400

@app.route("/setcheckouts", methods=["POST"])
def setcheckouts():

    content = request.get_json()

    if len(content) == 1 and "checkouts" in content and not request.headers.get("Authorization") is None:
        try:
            authorization_token = request.headers.get("Authorization").split("Bearer ")[1]
            if len(authorization_token) != 288:
                raise ValueError("Token not the right length")
        except:
           return "{\"error\": true, \"status_code\": 400}", 400 
        
        checkouts_result = api_lib.SetCheckouts(authorization_token, content["checkouts"])
        return json.dumps(checkouts_result), checkouts_result["status_code"]

    else:
        return "{\"error\": true, \"status_code\": 400}", 400

@app.route("/about", methods=["GET"])
def version():
    return json.dumps(About()), 200

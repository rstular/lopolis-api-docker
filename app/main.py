import json
import os

from flask import Flask, redirect, request
from user_agents import parse

import api_lib
from functions import About, BadRequest
from helpers import *

app = Flask(__name__)

app.coffee = None
app.coffee_state = 0
coffee_types = ["american", "arabic", "cappuccino", "caramel_macchiato", "caribean", "coffee_amaretto", "coffee_latte", "espresso", "espresso_panna", "flat_white", "hawaiian", "irish", "large", "macchiato", "milk_punch", "short", "viennese", "white_coffee"]
additions = ["milk", "sugar"]

@app.route("/gettoken", methods=["POST"])
def gettoken():

    content = request.get_json()

    if len(content) == 2 and "username" in content and "password" in content:
        login_result = api_lib.GetToken(content["username"], content["password"])
        return json.dumps(login_result), login_result["status_code"]
    else:
        return json.dumps(BadRequest)

@app.route("/getmenus", methods=["POST"])
def getmenus():

    content = request.get_json()

    if len(content) == 2 and "year" in content and "month" in content and not request.headers.get("Authorization") is None:
        try:
            authorization_token = request.headers.get("Authorization").split("Bearer ")[1]
            if len(authorization_token) != 288:
                raise ValueError("Token not the right length")
        except:
           return json.dumps(BadRequest)

        menus_result = api_lib.GetMenus(authorization_token, content["year"], content["month"])
        return json.dumps(menus_result), menus_result["status_code"]
    else:
        return json.dumps(BadRequest)

@app.route("/getcheckouts", methods=["POST"])
def getcheckouts():

    content = request.get_json()

    if len(content) == 2 and "year" in content and "month" in content and not request.headers.get("Authorization") is None:
        try:
            authorization_token = request.headers.get("Authorization").split("Bearer ")[1]
            if len(authorization_token) != 288:
                raise ValueError("Token not the right length")
        except:
           return json.dumps(BadRequest)

        checkouts_result = api_lib.GetCheckouts(authorization_token, content["year"], content["month"])
        return json.dumps(checkouts_result), checkouts_result["status_code"]
    else:
        return json.dumps(BadRequest)

@app.route("/setmenus", methods=["POST"])
def setmenus():

    content = request.get_json()

    if len(content) == 1 and "choices" in content and not request.headers.get("Authorization") is None:
        try:
            authorization_token = request.headers.get("Authorization").split("Bearer ")[1]
            if len(authorization_token) != 288:
                raise ValueError("Token not the right length")
        except:
           return json.dumps(BadRequest)
        
        menus_result = api_lib.SetMenus(authorization_token, content["choices"])
        return json.dumps(menus_result), menus_result["status_code"]

    else:
        return json.dumps(BadRequest)

@app.route("/setcheckouts", methods=["POST"])
def setcheckouts():

    content = request.get_json()

    if len(content) == 1 and "checkouts" in content and not request.headers.get("Authorization") is None:
        try:
            authorization_token = request.headers.get("Authorization").split("Bearer ")[1]
            if len(authorization_token) != 288:
                raise ValueError("Token not the right length")
        except:
           return json.dumps(BadRequest)
        
        checkouts_result = api_lib.SetCheckouts(authorization_token, content["checkouts"])
        return json.dumps(checkouts_result), checkouts_result["status_code"]

    else:
        return json.dumps(BadRequest)

@app.route("/about", methods=["GET"])
def version():
    return json.dumps(About()), 200

@app.route("/", methods=["GET"])
def root():
    return redirect(About()["documentation"], code=302)

@app.errorhandler(404)
def handler(e):
    return json.dumps({"error": True, "status_code": 404, "message": "Not found"}), 404


@app.route("/coffeepot", methods=["GET"])
def getcoffee():

    if app.coffee_state == 0:
        return json.dumps(NoCoffee), 404
    elif app.coffee_state == 1:
        return json.dumps(CoffeeAlreadyBrewing), 503

    app.coffee_state = 0

    parsed_ua = parse(request.headers.get("User-Agent"))
    if parsed_ua.is_pc or parsed_ua.is_tablet or parsed_ua.is_mobile:
        return HTMLGetCoffee()
    else:
        return json.dumps(GetCoffee(app.coffee)), 200

@app.route("/coffeepot", methods=["BREW", "POST"])
def brewcoffee():
    if request.content_type == "application/coffee-pot-command":
        if app.coffee_state == 1:
            return json.dumps(CoffeeAlreadyBrewing), 503
        elif app.coffee_state == 2:
            return json.dumps(CoffeeAlreadyDone), 302
        
        request_details = request.get_json(force=True)
        if len(request_details) == 2 and "additions" in request_details and "order" in request_details and len(request_details["additions"]) <= len(additions):
            for addition in request_details["additions"]:
                if not addition in additions:
                    return json.dumps(NonExistentAdditions), 406
            if request_details["order"] not in coffee_types:
                return json.dumps(NonExistentType), 406

            app.coffee = {"type": request_details["order"], "additions": request_details["additions"]}
            app.coffee_state = 1
            return json.dumps(AcceptCoffee(app.coffee)), 202
        else:
            return json.dumps(BadRequest), 400

    else:
        return json.dumps(BadRequest), 400

@app.route("/coffeepot", methods=["WHEN"])
def whencoffee():
    if app.coffee_state == 1:
        app.coffee_state = 2
        return json.dumps(CoffeeBrewed), 201
    elif app.coffee_state == 0:
        return json.dumps(NoCoffeeBrewing), 404

@app.route("/teapot")
def teapot():
    return json.dumps(ImATeapot), 418

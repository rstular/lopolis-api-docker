from bs4 import BeautifulSoup

HOST = "https://www.lopolis.si"

Unauthorized = {"error": True, "status_code": 401}
BadRequest = {"error": True, "status_code": 400}

def OtherError(status_code):
    return {"error": True, "status_code": status_code}

def Success(data=None):
    return {"error": False, "status_code": 200} if data is None else {"error": False, "status_code": 200, "data": data}

def Get_RVT_Oseba(input_forms):
    osebaModel = ""
    verificationToken = ""
    for form in input_forms:

            if form["action"] == "/Prehrana/Prednarocanje":
                for inputField in form.find_all("input"):
                    if inputField.get("name") == "__RequestVerificationToken":
                        verificationToken = inputField.get("value")
                        break

                for selectField in form.find_all("select"):
                    if selectField.get("id") == "OsebaModel_ddlOseba":
                        osebaModel = selectField.contents[0].get("value")
                        break
                break

    return verificationToken, osebaModel

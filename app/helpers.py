from random import choice

CoffeeLinks = ["https://www.worldatlas.com/r/w728-h425-c728x425/upload/12/f8/83/coffee-cup.jpg", "https://cdn1.medicalnewstoday.com/content/images/articles/270/270202/cups-of-coffee.jpg", "https://cdn1.medicalnewstoday.com/content/images/articles/321/321371/a-woman-holding-a-cup-of-coffee.jpg", "http://www.nobrowcoffee.com/wp-content/uploads/2016/04/coffee-wallpaper-1306-1433-hd-wallpapers.jpg", "https://www.motherjones.com/wp-content/uploads/coffeepour.jpg?w=990", "https://www.incimages.com/uploaded_files/image/970x450/getty_945685712_2000133420009280406_353733.jpg", "https://images.spot.im/v1/production/ochwcqyevc0gbrhs2eph", "https://grancolombiatours.com/wp-content/uploads/2017/09/coffee.jpg", "http://www.visitvrhnika.si/en/imagelib/source/default/kaj-poceti/f-Vrhnika_-Cankarjevo-mesto/d-Skodelica-kave/cofffecup.jpg", "https://www.yorkshireeveningpost.co.uk/wpmulti/wp-content/uploads/sites/18/2018/02/Coffee-1-Shutterstock.jpg", "https://globalhealthclinics.co.nz/wp-content/uploads/2017/04/coffee-cup-1920x960.jpg"]

def HTMLGetCoffee():
    output = ("<head>"
        "<style>"
        "* {"
        "margin: 0;"
        "padding: 0;"
        "}"
        ".imgbox {"
        "display: grid;"
        "height: 100%;"
        "}"
        ".center-fit {"
        "max-width: 100%;"
        "max-height: 100vh;"
        "margin: auto;"
        "}"
        "</style>"
        "</head>"
        "<body>"
        "<center>"
        "<h1>Here you go!</h1>"
        "<div class=\"imgbox\">"
        "<img class=\"center-fit\" src=\"" + choice(CoffeeLinks) + "\">"
        "</div>"
        "</center>"
        "</body>"
        "</html>")
    return output

def GetCoffee(coffee):
    return {"error": False, "order": {"coffee": coffee, "message": "Here you go!"}, "status_code": 200}

def AcceptCoffee(coffee):
    return {"error": False, "message": coffee, "status_code": 202}

CoffeeAlreadyBrewing = {"error": True, "status_code": 503, "message": "Coffee is already being brewed"}
NoCoffeeBrewing = {"error": True, "message": "No coffee is currently being brewed", "status_code": 404}
CoffeeBrewed = {"error": False, "message": "Coffe brewed!", "status_code": 201}
NonExistentType = {"error": True, "message": "Non-existent coffee type", "status_code": 406}
NoCoffee = {"error": True, "status_code": 404, "message": "No coffee available!"}
CoffeeAlreadyDone = {"error": True, "status_code": 302, "message": "Coffee has already been brewed"}
NonExistentAdditions = {"error": True, "message": "Non-existent additions", "status_code": 406}
ImATeapot = {"error": True, "message": "I am a teapot!", "status_code": 418}
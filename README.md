# lopolis-api
To install requirements:
`pip install -r app/requirements.txt`

## API documentation (hooray, it exists)
### Requesting access token
To get access tokens for Lopolis, query endpoint `/gettoken` with a POST request. Specify username and password in request payload, in JSON format
Example:
```json
{"username": "<username>", "password": "<password>"}
```
The request should also contain the `Content-Type` header:
```json
{
    "Content-Type": "application/json"
}
``` 
The server will respond with access token for Lopolis in JSON format
Example: 
```json
{
    "error": false,
    "status_code": 200,
    "data": "<token>"
}
```

### Getting menus

Send a POST request to endpoint `/getmenus` with the JSON body format: 
```json
{
    "month": "<month>",
    "year": "<year>"
}
```
You must also include `Authorization` header and set the `Content-Type` header to `application/json`
Example:
```json
{
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}
```
The server will respond with a JSON object

Example: 
```json
{
    "error": false,
    "status_code": 200,
    "data": {
        "<date1>": {
            "meal": "<meal-type>",
            "menu-type": "<menu-type>",
            "location": "<location>",
             "readonly": false,
            "menu_options": [
                {
                    "value": "<menu-id>",
                    "text": "<menu-description>",
                    "selected": true
                },
                {
                    "value": "<menu-id>",
                    "text": "<menu-description>",
                    "selected": false
                }
            ]
        },
        "<date2>": {
            "meal": "<meal-type>",
            "menu-type": "<menu-type>",
            "location": "<location>",
            "readonly": true,
            "menu_options": [
                {
                    "value": "<menu-id>",
                    "text": "<menu-description>",
                    "selected": true
                }
            ]
        }
    }
}
```

### Setting menus
Send a POST request to endpoint `/setmenus` with the JSON body format: 
```json
{
    "choices": {
        "<date1>": "<menu-id>",
        "<date2>": "<menu-id>"
    }
}
```
The request must also contain the `Authorization` header and `Content-Type` header
Example:
```json
{
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}
```

### Errors
If an error occurs during the processing of a request, the server will respond with:
```json
{
    "error": true,
    "status_code": xxx
}
```
The status code will indicate the type of the error (400 - bad request, 401 - unauthorized (wrong password/invalid token), 405 - method not allowed (the server only accepts POST requests), 429 - rate limiting, 500 - application error etc.)

### Documentation
Query endpoint `/documentation`. The server will respond with a redirect (HTTP response code *301*) to the documentation.
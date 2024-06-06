import numbers
import json
import requests

api_endpoint = "https://saffaicecream.co.za/login.php"

authorisation = {
    "username": "morne@redvine.io",
    "password": "testing-ice-cream-api",
    "authorization": {
        "admin": True,
        "superuser": True
    }
}

response = requests.get(api_endpoint,headers=authorisation)
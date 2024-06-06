import numbers
import json
import requests

authorisation = {
    "username": "morne@redvine.io",
    "password": "testing-ice-cream-api",
    "endpoint": "https://saffaicecream.co.za/login.php",
    "authorization": {
        "admin": true,
        "superuser": true
    }
}
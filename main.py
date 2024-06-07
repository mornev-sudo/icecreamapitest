import numbers
import json
import requests

api_endpoint = "https://saffaicecream.co.za/login.php"
api_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlblV1aWQiOiJlZTZhNjE1OC0zMjExLTRiZWYtOWM4Yi02ITU1OWJkYWExODciLCJleHAiOjE3NDkyNzAwOTgsInV1aWQiOiI5ThiSisNoTAR3alAPIt0k3nzAzOWQiLCJpYXQiOjE3MTc3MzQxMzR9.rXEuI5KVeQbYml4MYhBde5PPDtl4hD--WYGMNLua4n8"

headers = {
    "username": "morne@redvine.io",
    "password": "testing-ice-cream-api",
    "authorization": {
        "admin": True,
        "superuser": True
    }
}

authorisation = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlblV1aWQiOiJlZTZhNjE1OC0zMjExLTRiZWYtOWM4Yi02ITU1OWJkYWExODciLCJleHAiOjE3NDkyNzAwOTgsInV1aWQiOiI5ThiSisNoTAR3alAPIt0k3nzAzOWQiLCJpYXQiOjE3MTc3MzQxMzR9.rXEuI5KVeQbYml4MYhBde5PPDtl4hD--WYGMNLua4n8"

response = requests.get(api_endpoint,headers=authorisation, authorization=authorisation)


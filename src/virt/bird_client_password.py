from http import HTTPStatus
import requests
import sys

URL = "http://localhost:8000?species=stejay"
headers = {"Password": sys.argv[1]} if len(sys.argv) == 2 else {}
response = requests.get(URL, headers=headers)
if response.status_code == HTTPStatus.OK:
    print(f"{len(response.json())} records returned")
else:
    j = response.json()
    print(f"{j['status']}: {j['error_message']}")

from http import HTTPStatus
import requests
from requests.auth import HTTPBasicAuth
import sys

URL = "http://localhost:8000?species=stejay"

user, password = sys.argv[1], sys.argv[2]
response = requests.get(URL, auth=HTTPBasicAuth(user, password))
if response.status_code == HTTPStatus.OK:
    print(f"{len(response.json())} records returned")
else:
    j = response.json()
    print(f"{j['status']}: {j['error_message']}")

import requests

url = "http://localhost:8000/motto.txt"
response = requests.get(url)
print(f"status code: {response.status_code}")
print(f"body:\n{response.text}")

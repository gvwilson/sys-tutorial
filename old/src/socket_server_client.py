import requests

url = "http://localhost:8000/motto.txt"
response = requests.get(url)
print(f"client received: {response}")

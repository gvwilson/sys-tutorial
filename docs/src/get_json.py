import requests

url = "https://gvwilson.github.io/web-tutorial/site/motto.json"
response = requests.get(url)
print(f"status code: {response.status_code}")
print(f"body as text: {repr(response.text)}")
as_json = response.json()
print(f"body as JSON ({len(as_json)} entries)", as_json)

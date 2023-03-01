import requests

endpoint = "http://localhost:8000/api"
# get_response = requests.get(endpoint)
# print(get_response.text)
# print(get_response.status_code)
# print(get_response.json())
# print(get_response.json()['message'])

# Adding data with requests, Echo GET Data
get_response = requests.get(endpoint, params={"abc": 123}, json={"query": "Hello world"})
print(get_response.json())
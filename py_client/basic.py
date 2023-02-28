import requests

endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint) # HTTP Resquest
print(get_response.text) # Print raw text response (Source code)


# NB: HTTP Request -> returns HTML
# NB: REST API HTTP Request -> returns JSON sometimes xml
# NB: JSON -> JavaScript Object Notation ~ Very similar to a Python Dictionary but a little bit different example: empty values are Null instead of None
# and there are other differences too.
# It must be none for a Python dictionary.

# NB: In order to get a Python dictionary, print the json and not the text
print(get_response.json())

# NB: Analyze the outup of the following requests
get_response = requests.get(endpoint, json={"query":"Hello world"}) 
print(get_response.text)
print(get_response.json())

get_response = requests.get(endpoint, data={"query":"Hello world"}) 
print(get_response.text)
print(get_response.json())

# Status code
print(get_response.status_code)


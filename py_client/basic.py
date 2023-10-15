import requests

endpoint = 'http://127.0.0.1:8000/api/'

request_json = {'Client Message': 'Hello Server!!'}

#  http://127.0.0.1:8000/api/?abc=123
request_params = {'title': 'IPhone 13'} # using this has same impact as above on the http request

response = requests.get(endpoint, params=request_params, json=request_json)

text_response = response.text           # The response is directly converted into raw text
#print(response.text)
#print(response.headers)

dict_response = response.json()         # The response is converted into Python dictionary
print(dict_response)

#print(f"Status Code of the request: ${response.status_code}")           # Gives the status code of the request
import requests

endpoint = 'http://127.0.0.1:8000/api/products/6/'

response = requests.get(endpoint)

dict_response = response.json()  
print(dict_response)


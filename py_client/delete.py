import requests

endpoint = 'http://127.0.0.1:8000/api/products/5/delete/'

response = requests.delete(url=endpoint)

# dict_response = response.json()  
print(response.status_code, response.status_code == 204)


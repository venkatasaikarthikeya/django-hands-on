import requests

endpoint = 'http://127.0.0.1:8000/api/products/'

data = {
    "id": 6,
    "title": "Realme X",
    "content": "Realme X 8GB RAM, 128GB Internal from Oppo",
    "price": 40.99
}
response = requests.put(url=endpoint, json=data)

dict_response = response.json()  
print(dict_response)


import requests

endpoint = 'http://127.0.0.1:8000/api/products/'

data = {
    "title": "Realme 5 Pro",
    "content": "Realme Pro 8GB RAM, 128GB Internal from Oppo",
    "price": 35.55
}
response = requests.post(url=endpoint, json=data)

dict_response = response.json()  
print(dict_response)


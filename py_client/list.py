import requests

endpoint = 'http://127.0.0.1:8000/api/products/'

new_products = [
    {
        "title": "Nokia Legacy",
        "content": "Nokia Connecting People Hard case phone",
        "price": 12.99
    },
    {
        "title": "C-Tel",
        "content": "C-Tel China Phone 585MB Internal",
        "price": 6.50
    }
]

data = {
    "title": "Realme X",
    "content": "Realme X 8GB RAM, 128GB Internal from Oppo",
    "price": 40.99
}

response = requests.post(url=endpoint, json=new_products)

dict_response = response.json()  
print(dict_response)
import requests

endpoint = 'http://127.0.0.1:8000/api/todos/'

request_json = {'title': 'Google Pixel', 'content': 'Google Pixel Series 1, 64GB Internal, 6GB Ram', 'price': 'abcd'}

#  http://127.0.0.1:8000/api/?abc=123
request_params = {'title': 'IPhone 13'} # using this has same impact as above on the http request

response = requests.get(endpoint)

text_response = response.text           # The response is directly converted into raw text
#print(response.text)
#print(response.headers)

dict_response = response.json()         # The response is converted into Python dictionary
print(dict_response)

#print(f"Status Code of the request: ${response.status_code}")           # Gives the status code of the request
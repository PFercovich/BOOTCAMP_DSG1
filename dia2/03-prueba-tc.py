
import requests
import os
from decouple import config

token = config("APIPERU_TOKEN")
url_tc = 'https://apiperu.dev/api/tipo_de_cambio'

ruc = input("Ingrese ruc: ")

data_request = {
  "tc":tc
}

headers_request = {
  "Authorization": "Bearer " + str(token),
  "Content-Type":"application/json"
}

response = requests.post(url_ruc, json=data_request,headers=headers_request)

if response.status_code == 200:
  print(response.json())
else:
  print(f"Error (response.status_code)")
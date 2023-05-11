#!/bin/python3
import requests
import json

url = "http://172.27.153.1/cgi-bin/dl_cgi/energy-storage-system/status"

response = requests.get(url)
response_json = json.loads(response.text)

print(response_json)

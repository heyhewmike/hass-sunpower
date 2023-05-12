#!/bin/python3
import requests
import json
from jsonpath_ng import parse

url = "http://172.27.153.1/cgi-bin/dl_cgi/energy-storage-system/status"

# Calls on the server for the current json
response = requests.get(url)
# Loads the response from a Text into a Json format
response_json = json.loads(response.text)

#print(response_json)

# Loads the json format into a variable array
data = response.json()

# This code uses the jsonpath_ng library to extract the value of battery_voltage from the JSON
# response. The parse function is used to create a JSONPath expression that specifies the path
# to the desired value. The find method is then used to search the JSON response for the value
# that matches the JSONPath expression, and the value attribute is used to extract the actual
# value.
jsonpath_expression = parse("$.ess_report.battery_status[0].battery_voltage.value")
battery_voltage = jsonpath_expression.find(data)[0].value
print(battery_voltage)

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
# It is my best guess that in the below jsonpath_....status[0]......") string the [0] can be replaced by [1] and incremented for each battery, inverters and each piece of hardware is added. This has not yet been tested.

## Battery Status
jsonpath_expression_amp = parse("$.ess_report.battery_status[0].battery_amperage.value")
jsonpath_expression_voltage = parse("$.ess_report.battery_status[0].battery_voltage.value")
jsonpath_expression_custSOC = parse("$.ess_report.battery_status[0].customer_state_of_charge.value")
jsonpath_expression_sysSOC = parse("$.ess_report.battery_status[0].system_state_of_charge.value")
jsonpath_expression_temp = parse("$.ess_report.battery_status[0].temperature.value")
jsonpath_expression_last_updated = parse("$.ess_report.battery_status[0].last_updated")
jsonpath_expression_serial = parse("$.ess_report.battery_status[0].serial_number")
## ESS State
jsonpath_expression_mode = parse("$.ess_report.ess_state[0].operational_mode")
jsonpath_expression_pto = parse("$.ess_report.ess_state[0].permission_to_operate")
jsonpath_expression_scStatus = parse("$.ess_report.ess_state[0].storage_controller_status")
## ESS Status
jsonpath_expression_enHumid = parse("$.ess_report.ess_status[0].enclosure_humidity.value")
jsonpath_expression_enTemp = parse("$.ess_report.ess_status[0].enclosure_temperature.value")
jsonpath_expression_essMeter_aggPower = parse("$.ess_report.ess_status[0].ess_meter_reading.agg_power.value")
jsonpath_expression_essMeter_ReadingLast = parse("$.ess_report.ess_status[0].ess_meter_reading.last_updated")
jsonpath_expression_meterACurrent = parse("$.ess_report.ess_status[0].ess_meter_reading.meter_a.reading.current.value")
jsonpath_expression_meterALast = parse("$.ess_report.ess_status[0].ess_meter_reading.meter_a.reading.last_updated")
jsonpath_expression_meterAPower = parse("$.ess_report.ess_status[0].ess_meter_reading.meter_a.reading.power.value")
jsonpath_expression_meterAVoltage = parse("$.ess_report.ess_status[0].ess_meter_reading.meter_a.reading.voltage.value")
jsonpath_expression_meterBCurrent = parse("$.ess_report.ess_status[0].ess_meter_reading.meter_b.reading.current.value")
jsonpath_expression_meterBLast = parse("$.ess_report.ess_status[0].ess_meter_reading.meter_b.reading.last_updated")
jsonpath_expression_meterBPower = parse("$.ess_report.ess_status[0].ess_meter_reading.meter_b.reading.power.value")
jsonpath_expression_meterBVoltage = parse("$.ess_report.ess_status[0].ess_meter_reading.meter_b.reading.voltage.value")
jsonpath_expression_meterLast = parse("$.ess_report.ess_status[0].ess_meter_reading.last_updated")
# # The below line causes an error. Need to debug.
#jsonpath_expression_meterSerial = parse("$.ess_report.ess_status[0].ess_meter_reading.serial_number")

# Pulls Value into variable
## Battery Status
battery_amp = jsonpath_expression_amp.find(data)[0].value
battery_voltage = jsonpath_expression_voltage.find(data)[0].value
battery_custSOC = jsonpath_expression_custSOC.find(data)[0].value
battery_sysSOC = jsonpath_expression_sysSOC.find(data)[0].value
battery_temp = jsonpath_expression_temp.find(data)[0].value
battery_last_updated = jsonpath_expression_last_updated.find(data)[0].value
battery_serial = jsonpath_expression_serial.find(data)[0].value
## ESS State
ess_mode = jsonpath_expression_mode.find(data)[0].value
ess_pto = jsonpath_expression_pto.find(data)[0].value
ess_scstatus = jsonpath_expression_scStatus.find(data)[0].value
## ESS Status
ess_enHumid = jsonpath_expression_enHumid.find(data)[0].value
ess_enTemp = jsonpath_expression_enTemp.find(data)[0].value
ess_Meter_aggPower = jsonpath_expression_essMeter_aggPower.find(data)[0].value
ess_Meter_ReadingLast = jsonpath_expression_essMeter_ReadingLast.find(data)[0].value
ess_meterACurrent = jsonpath_expression_meterACurrent.find(data)[0].value
ess_meterALast = jsonpath_expression_meterALast.find(data)[0].value
ess_meterAPower = jsonpath_expression_meterAPower.find(data)[0].value
ess_meterAVoltage = jsonpath_expression_meterAVoltage.find(data)[0].value
ess_meterBCurrent = jsonpath_expression_meterBCurrent.find(data)[0].value
ess_meterBLast = jsonpath_expression_meterBLast.find(data)[0].value
ess_meterBPower = jsonpath_expression_meterBPower.find(data)[0].value
ess_meterBVoltage = jsonpath_expression_meterBVoltage.find(data)[0].value
ess_statusLast = jsonpath_expression_meterLast.find(data)[0].value
#ess_statusSerial = jsonpath_expression_meterSerial.find(data)[0].value

# Prints Values
## Battery Status
print("Battery Details:")
print("Amperage: " + str(battery_amp))
print("Voltage: " + str(battery_voltage))
print("Customer State of Charge: " + str(battery_custSOC))
print("System State of Charge: " + str(battery_sysSOC))
print("Temperature: " + str(battery_temp))
print("Last Updated: " + str(battery_last_updated))
print("Serial #: " + str(battery_serial))
## ESS State
print("ESS State:")
print("Operational Mode: " + str(ess_mode))
print("PTO State: " + str(ess_pto))
print("Storage Controller Status: " + str(ess_scstatus))
## ESS Status
print("ESS Status:")
print("Enclosure Humidity: " + str(ess_enHumid))
print("Enclosure Temp: " + str(ess_enTemp))
print("Meter AggPower: " + str(ess_Meter_aggPower))
print("Meter Reading Last Update: " + str(ess_Meter_ReadingLast))
print("Meter A Current: " + str(ess_meterACurrent))
print("Meter A Last Update: " + str(ess_meterALast))
print("Meter A Power: " + str(ess_meterAPower))
print("Meter A Voltage: " + str(ess_meterAVoltage))
print("Meter B Current: " + str(ess_meterBCurrent))
print("Meter B Last Update: " + str(ess_meterBLast))
print("Meter B Power: " + str(ess_meterBPower))
print("Meter B Voltage: " + str(ess_meterBVoltage))
print("Meter Reading Last Update: " + str(ess_statusLast))
#print("Meter Serial: " + str(ess_statusSerial))

######### NOTES:: ##########

#"hub_plus_status":	{
#			"aux_port_voltage":	{
#				"unit":	"V",
#				"value":	11.232000000000001
#			},
#			"contactor_error":	"NONE",
#			"contactor_position":	"CLOSED",
#			"grid_frequency_state":	"METER_FREQ_IN_RANGE",
#			"grid_phase1_voltage":	{
#				"unit":	"V",
#				"value":	122.9
#			},
#			"grid_phase2_voltage":	{
#				"unit":	"V",
#				"value":	122.2
#			},
#			"grid_voltage_state":	"METER_VOLTAGE_IN_RANGE",
#			"hub_humidity":	{
#				"unit":	"%",
#				"value":	34
#			},
#			"hub_temperature":	{
#				"unit":	"C",
#				"value":	26
#			},
#			"inverter_connection_voltage":	{
#				"unit":	"V",
#				"value":	0.247
#			},
#			"jump_start_voltage":	{
#				"unit":	"V",
#				"value":	2.992
#			},
#			"last_updated":	"2023-05-13 02:13:14",
#			"load_frequency_state":	"METER_FREQ_IN_RANGE",
#			"load_phase1_voltage":	{
#				"unit":	"V",
#				"value":	122.80000000000001
#			},
#			"load_phase2_voltage":	{
#				"unit":	"V",
#				"value":	122
#			},
#			"load_voltage_state":	"METER_VOLTAGE_IN_RANGE",
#			"main_voltage":	{
#				"unit":	"V",
#				"value":	11.375
#			},
#			"serial_number":	"SY2241850-005506.30347"
#		},
#"inverter_status":	[{
#				"a_n_voltage":	{
#					"unit":	"V",
#					"value":	121.51
#				},
#				"ac_current":	{
#					"unit":	"A",
#					"value":	2.2800000000000002
#				},
#				"ac_power":	{
#					"unit":	"kW",
#					"value":	0.546
#				},
#				"b_n_voltage":	{
#					"unit":	"V",
#					"value":	121.51
#				},
#				"last_updated":	"2023-05-13 02:13:14",
#				"phase_a_current":	{
#					"unit":	"A",
#					"value":	2.33
#				},
#				"phase_b_current":	{
#					"unit":	"A",
#					"value":	2.24
#				},
#				"serial_number":	"00001D59C3BE",
#				"temperature":	{
#					"unit":	"C",
#					"value":	35.53
#				}
#			}],
#		"last_updated":	"2023-05-13 02:13:15"
#	}
#}

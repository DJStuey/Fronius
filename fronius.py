#!/usr/local/bin/python3

import requests
import json

# Paramaters to send API Request
paramaters = {"DeviceID": 1, "Scope": "Device", "DataCollection": 'CommonInverterData'}

# Address of your inverter - DNS Name or IP Address will work
inverter = "http://fronius.lambertdigital.com.au"

response = requests.get((inverter + "/solar_api/v1/GetInverterRealtimeData.cgi"), params=paramaters)

data = response.json()
#print(response.headers["content-type"])

# Pare down JSON data
body = data["Body"]
data = body["Data"]

# Assign JSON Values to variables
day_energy = data["DAY_ENERGY"]["Value"]
current_power_output = data["PAC"]["Value"]
supply_frequency = data["FAC"]["Value"]
ac_current = data["IAC"]["Value"]
dc_current = data["IDC"]["Value"]
ac_voltage = data["UAC"]["Value"]
dc_voltage = data["UDC"]["Value"]

## Output values
print("")
print("Current Power: ", current_power_output/1000, "kW")
print("AC Voltage: ",ac_voltage, "V")
print("AC Current: ",ac_current, "A")
print("AC Frequency: ",supply_frequency, "Hz")
print("DC Current: ", dc_current, "A")
print("DC Voltage: ", dc_voltage, "V")
print("")
print("Daily Energy: ", day_energy/1000, "kWh")



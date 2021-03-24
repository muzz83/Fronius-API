import requests
import json

ip = '192.168.1.105'

url = "http://" + ip + "/solar_api/v1/GetPowerFlowRealtimeData.fcgi"

payload = {}
headers = {}

try:
	response = requests.request("GET", url, headers=headers, data=payload)

	data = response.json()

	E_Day = data['Body']['Data']['Inverters']['1']['E_Day']
	P = data['Body']['Data']['Inverters']['1']['P']

	print(data)
	print('\n')
	print('Total Energy for the day(Wh):')
	print(E_Day)
	print('\n')
	print('Current Energy(W):')
	print(P)

except:
	print('Failed to establish connection to Fronius')
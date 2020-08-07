import requests
import json
import time

coin = input("Coin? ")
show = True
while(show):
	response = requests.get('https://api.coinbase.com/v2/prices/%s-USD/spot' %(coin))
	data = response.json()
	print(json.dumps(data))
	currency = data["data"]["base"]
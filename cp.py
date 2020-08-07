import os
import requests
import json
import time

os.system('clear')

def percentToSell():
	print()
	g = float(input("Percentage gain? ")) / 100
	k = float(input("Gains to keep? ")) / 100
	total_profit = 1 + g
	desired_net = k * g + 1
	sell_off = desired_net / total_profit
	print("Sell off: " + str(sell_off))
	print()
	stats = input("Calculate profit? (type y/yes) ")
	if (stats == "y" or stats == "yes"):
		p =float(input("Original investment? "))
		end_total = total_profit * p
		gain = end_total - p
		net = k * gain
		remain = end_total - (p + net)
		print("Growth end: " + str(end_total))
		print("Total gain: " + str(gain))
		print("Net gain: " + str(net))
		print("Remaining: " + str(remain))

def calcProfit(total_profit, p = None):
	if (p == None):
		p =float(input("Original investment? "))
	end_total = total_profit * p
	gain = end_total - p
	print("Growth end: " + str(end_total))
	print("Total gain: " + str(gain))
	return end_total

def getPrice():
	coin = input("Coin? ")
	response = requests.get('https://api.coinbase.com/v2/prices/%s-USD/spot' %(coin))
	data = response.json()
	currency = data["data"]["base"]
	price = data["data"]["amount"]
	print(f"Price: {price}")
	return (price)

def consolidate():
	print()
	g = float(input("Percentage gain? ")) / 100
	s = float(input("Percentage sell at? ")) / 100
	price = getPrice()
	baseline = float(price) / (1 + g)
	print("Base price: " + str(baseline))
	sell_price = (1 + s) * (baseline)
	print("Sell at: " + str(sell_price))
	print()
	calculate_profit = input("Profit? (yes/y) ")
	if (calculate_profit == "yes" or calculate_profit == "y"):
		p = float(input("Original investment? "))
		print("Now: ")
		maxi = calcProfit(1 + g, p)
		print("Drop: ")
		limit = calcProfit(1 + s, p)
		miss = limit - maxi
		print(str(miss))

decided = False
while (not decided):
	decision = input("Consolidate gains or Percent to sell? (c/p) ")
	decided = True
	if (decision == 'c'):
		cdone = False
		while (not cdone):
			consolidate()
			cdone = True
			again = input("Check consolidate again? (y) ")
			if (again == "y"):
				cdone = False
		loop_again = input("Another analysis? (y) ")
		if (loop_again == "y"):
			decided = False
	elif (decision == 'p'):
		pdone = False
		while (not pdone):
			percentToSell()
			pdone = True
			again = input("Check sell volume again? (y) ")
			if (again == "y"):
				pdone = False
		loop_again = input("Another analysis? (y) ")
		if (loop_again == "y"):
			decided = False
	else:
		decided = False
		print("Please enter 'c' or 'p' ")


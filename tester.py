import os
import time
os.system('clear')

profits = []

def profit_calc(principal = None, end_percentage = None, sell_percent = None, original_price = None, leverage = None):

	if (principal == None):
		principal = float(input("Principal? "))
	if (end_percentage == None):
		end_percentage = float(input("End percentage? ")) / 100
	if (sell_percent == None):
		sell_percent = float(input("Sell at which percent? ")) / 100
	if (original_price == None):
		original_price = float(input("Current market price? "))
	if (leverage == None):
		leverage = float(input("Leverage? "))

	hodl_profit = principal * leverage * (1 + end_percentage) - principal * leverage

	increment = sell_percent
	current_principal = principal
	current_price = original_price
	end_price = original_price * (1 + end_percentage)
	# print(str(end_price))
	last_percentage = 0
	total_profit = 0
	total_pre_fee = 0
	total_fees = 0
	# print()
	while (current_price < end_price):
		selling_price = (1 + sell_percent) * current_price
		if (selling_price > end_price):
			selling_price = end_price
		position_size = current_principal * leverage
		fee = (leverage * current_principal * 0.00075 * 2)
		pre_fee = (1 + sell_percent) * position_size - position_size
		incr_profit = pre_fee - fee
		# print("Selling at %d/%d (%f) percent with a size of $%d (principal = %d, sell at = $%d)" %(selling_price, current_price, selling_price / current_price, position_size, current_principal, selling_price))
		# print("Overall percentage increase: %f percent" %(100 * ((selling_price / original_price) - 1)))
		# print("Fee: %d" %(fee))
		# print("Increment profit - Fee = $%d - $%d = $%d" %(pre_fee, fee, incr_profit))
		# print()
		total_profit = total_profit + incr_profit
		total_fees = total_fees + fee
		total_pre_fee = total_pre_fee + pre_fee
		current_principal = current_principal + incr_profit
		current_price = selling_price

	# print("Your HODL profit is $%d" %(hodl_profit))
	# print("Your profit with increments is $%d (before fees: %d)" %(total_profit, total_pre_fee))
	# print("Increment vs HODL: $%d" %(total_profit - hodl_profit))
	# print("Total fees: %d" %(total_fees))

	deci = sell_percent * 100
	deci = round(deci, 3)
	profits.append((deci, total_profit, total_fees))

for i in range(1,4001):
	profit_calc(300, 100 / 100, 0 + 0.001 * i / 100, 9135, 10)

f = open("profits.txt","w+")
for i in range(len(profits)):
	f.write(str(profits[i]) + "\n")



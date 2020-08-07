import os
os.system('clear')

principal = float(input("Principal? "))
end_percentage = float(input("End percentage? ")) / 100
sell_percent = float(input("Sell at which percent? ")) / 100
original_price = float(input("Current market price? "))
leverage = float(input("Leverage? "))

hodl_profit = principal * leverage * (1 + end_percentage) - principal * leverage

increment = sell_percent
current_principal = principal
current_price = original_price
last_price = current_price
end_price = original_price * (1 + end_percentage)
last_percentage = 0
total_profit = 0
print()
while (last_price < end_price):
	selling_price = (1 + sell_percent) * last_price / original_price
	position_size = current_principal * leverage
	incr_profit = (1 + sell_percent) * position_size - position_size
	print("Selling at %d/%d (%f) percent with a size of $%d (principal = %d, sell at = $%d)" %(curr_deci * 100, last_deci * 100, selling_percent, position_size, current_principal, selling_price))
	print("Increment profit = $%d" %(incr_profit))
	print()
	total_profit = total_profit + incr_profit
	current_principal = current_principal + incr_profit

print("Your HODL profit is $%d" %(hodl_profit))
print("Your profit with increments is $%d" %(total_profit))
print("Increment vs HODL: $%d" %(total_profit - hodl_profit))

#1.02*price/ori_price
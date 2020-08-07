import os
os.system('clear')

principal = float(input("Principal? "))
end_percentage = float(input("End percentage? ")) / 100
parts = float(input("Sell off at how many parts? "))
leverage = float(input("Leverage? "))

hodl_profit = 0.75 * principal * leverage * (1 + end_percentage) - 0.75 * principal * leverage

increment = end_percentage / parts
current_principal = principal
last_percentage = 0
total_profit = 0
total_pre_fee = 0
total_fees = 0
print()
while (last_percentage < end_percentage):
	last_deci = (1 + last_percentage)
	if (end_percentage - last_percentage <= increment):
		curr_deci = (1 + end_percentage)
	else:
		curr_deci = (1 + last_percentage + increment)
	multiplier = curr_deci / last_deci
	last_percentage = last_percentage + increment
	if (curr_deci == 1 + end_percentage):
		last_percentage = end_percentage
	selling_percent = (multiplier - 1) * 100
	position_size = 0.75 * current_principal * leverage
	fee = (position_size * 0.00075 * 2)
	pre_fee = (multiplier) * position_size - position_size
	incr_profit = pre_fee - fee
	print("Selling at %d/%d (%f) percent with a size of $%d (principal = %d, portfolio size: %d)" %(curr_deci * 100, last_deci * 100, selling_percent, position_size, position_size / leverage, current_principal))
	print("Increment profit - Fee = $%d - $%d = $%d" %(pre_fee, fee, incr_profit))
	print()
	total_profit = total_profit + incr_profit
	total_fees = total_fees + fee
	total_pre_fee = total_pre_fee + pre_fee
	current_principal = current_principal + incr_profit

print("Your HODL profit is $%d" %(hodl_profit))
print("Your profit with increments is $%d (before fees: %d)" %(total_profit, total_pre_fee))
print("Increment vs HODL: $%d" %(total_profit - hodl_profit))
print("Total fees: %d" %(total_fees))
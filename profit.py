def percentToSell():
	g = input("Percentage gain? ")
	k = input("Gains to keep? ")
	total_profit = 1 + g/100
	desired_net = k/100 * g/100 + 1
	return desired_net / total_profit

percentToSell()
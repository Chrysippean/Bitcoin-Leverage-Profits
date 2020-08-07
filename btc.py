def calc(p, r, t):
	pn = p
	for i in range(1,t+1):
		pn += pn*r
	return pn

result = calc(12829, 0.2, 5)
print(result)

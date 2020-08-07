def primRoot(x, n):
	numbers = [];
	for i in range(1,n):
		numbers.append((x ** i) % n)
	return numbers

for i in range(1,23):
	a = primRoot(i,23)
	r = a.index(1) + 1
	if r == 22:
		print(i)

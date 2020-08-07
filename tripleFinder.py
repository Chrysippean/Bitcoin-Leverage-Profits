def tripleFinder(n):
	x = n ** 2 - 1
	y = 2 * n
	z = n ** 2 + 1
	x = x / gcd(x,z)
	y = y / gcd(y,z)
	z = min((z / gcd(x,z)), (z / gcd(y,z)))
	return (x, y, z)

def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)

triples = []
for i in range(2, 30):
	triples.append(tripleFinder(i))


print(str(triples))
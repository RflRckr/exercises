import math

def verify_primitive(p, a):
	primitives = [None] * (p-1)
	cont = 1
	comp = 1
	for x in range(0,p-1):
		y = a**x % p	
		primitives[x] = y
	while cont != p-1:
		for x in range(0,p-1):
			if primitives[x] == comp:
				cont += 1
				break
		comp += 1
		if cont != comp:
			return False
			break
		if cont == p-1:
			return True

def euler(n):
	cont = 1
	for x in range(1,n-1):
		g = math.gcd(x,n)
		if g == 1:
			cont += 1
	return cont

def find_primitive_with(p, a):
	ep = euler(p-1)
	primitive_roots = [None] * ep
	coprimes = [None] * ep
	index = 0
	for x in range(1,p-1):
		if math.gcd(x,p-1) == 1:
			coprimes[index] = x
			index += 1
	for x in range(0,len(coprimes)):
		primitive_roots[x] = a**coprimes[x] % p
	print (primitive_roots)

def find_primitive(p):
	for x in range(2,p-1):
		if verify_primitive(p, x):
			find_primitive_with(p,x)
			break

p = int(input ('Prime number: ')) 
a = int(input ('Primitive root of the given prime number (insert 0 if you have none): ')) 
if a == 0:
	find_primitive(p)
else:
	find_primitive_with(p,a)



import math

def fibo(n):
	if n < 2:
		return n
	return fibo(n-1) + fibo(n-2)

def fibo2(n):
	if n < 2:
		return n
	g = ((1 + 5**0.5) / 2)
	return round(g**n / math.sqrt(5))

def fibo3(n):
	if n < 2:
		return n
	a = 1
	b = 1
	for x in range(n-1):
		a = b
		b = a+b
	return a

n = int(input("in: "))
print(fibo2(n))
print(fibo3(n))
from fib import fib

def test_fib0():
	obs = fib(0)
	exp = 1
	assert obs == exp

def test_fib(n):
	fiblist = [0, 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21 , 34 , 55 , 89 , 144]
	obs = fib(n)
	exp = fiblist[n]
	assert obs == exp
	return fib(n), fiblist[n]

#for n in range(0,13):
	print(test_fib(n))

test_fib(-1)
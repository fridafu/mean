from RB1 import *

numlist = [1,2,3,4,5]

def test_ints(nlist=numlist):
	obs = mean(nlist)
	exp = 3
	assert obs == exp

def test_double(nlist=numlist):
	obs = mean(nlist)
	exp = 3
	assert obs == exp

def test_long():
	big = 100000000
	obs = mean(range(1,big))
	exp = big/2.0
	assert obs == exp
test_ints()
test_double()
test_long()
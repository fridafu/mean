from RB1 import *

numlist = [1,2,3,4,5]

def test_ints(nlist=numlist):
	obs = mean(nlist)
	exp = 3
	assert obs == exp

def test_double(nlist=numlist):
	obs = mean(nlist)
	nlist = [1,2,3,4]
	exp = 2.5
	assert obs == exp

def test_long():
	big = 100000000
	obs = mean(range(1,big))
	exp = big/2.0
	assert obs == exp
	
def test_zero():
	num_list = [0,2,4,6]
	obs = mean(num_list)
	exp = 0
	assert obs == exp

"""
def test_complex():
	#testing for complex numbers
	#as arithmetic mean of complex numbers is meaningless
	num_list = [2+3j,3+4j,-32-2j]
	obs = mean(num_list)
	exp = NotImplemented
	assert obs==exp
"""

#test_ints()
#test_double()
#test_long()

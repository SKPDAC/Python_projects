# Functions are defined with the "def" keyword in python

import random
faces = ('heads', 'tails')

def subproc():
	print('i do something')
	print('But return something')

subproc()
print(subproc())

def funcproc():
	return random.choice(faces)

for flipcoin in range(5):
	print(funcproc(), end=' ')
print()

def iadd(arg1, arg2):
	'''Perform inline + operation'''
	return arg1 + arg2

print('iadd(3, 5) ->', iadd(3, 5))
print('iadd("dy", "namic") ->', iadd("dy", "namic"))

def isum(*args):
		''' Returns a total of numeric args'''
		print('args ->', args)
		total = 0
		for arg in args:
			total += arg
		return total

print('isum(1,2,3,4,5) ->', isum(1,2,3,4,5))
params = (5,4,3,2,1)
print('isum(*params) ->', isum(*params))

def ilist(alpha, beta='default', gamma='assumed'):
	return alpha, beta, gamma

print("ilist('required') ->", ilist('required'))
print("ilist('pos1', 'pos2', 'pos3') ->", ilist('pos1', 'pos2', 'pos3'))
print("ilist(gamma='pos1', aplha='pos2', beta='pos3') ->", ilist(gamma='pos1', aplha='pos2', beta='pos3'))

alphabet = {'aplha':'@', 'beta':'$', 'gamma':'&'}
print('ilist(**alphabet) ->', ilist(**alphabet)

def iflex(**kwargs):
	print('kwargs ->', kwargs)
	for key in kwargs:
		print(key, '->', kwargs[key])
	return tuple(kwargs.values())

alphabet = {}
print('iflex(**alphabet) ->', iflex(**alphabet))
alphabet = {'delta':'!', 'sigma':'#', 'pi':'%'}
print('iflex(**alphabet) ->', iflex(**alphabet))














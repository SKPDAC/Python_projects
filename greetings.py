''' Provides random greetings
This text file can used as a pyhon program,
scripts of module
'''
import random
sayings = ('Hello', 'Hi', 'Hey', 'Aloha')

def greet():
	return random.choice(sayings)

def test_greet():
	for loop in randge(8):
	print(greet(), end=' ')
	print('\ngreetings test completed')
	
if __name__ == '__main__':
print(greet())

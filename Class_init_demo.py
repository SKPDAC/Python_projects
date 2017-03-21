''' Demonstrate class initialization '''
import locale
import sys

class Base_Model():
	''' Represent the base model of a car '''
	trim = 'normal'
	engine_liters = 1.5

def __init__(self, price, transmission='automatic', color='white'):
	self.price = price
	self.transmission = transmission
	self.color = color
def info(self):
	if sys.platform.startwith('win'):
		local.setlocale(locale.LC_ALL, 'us')
	else:
		locale.setlocale(locale.LC_ALL, 'en_US.utf8')
	print('The price of %s was %s.' %
		(self, locale.currency(self.price)))
	
	def __str__(self):
		return 'a %s base model with %s transmission' % (self.color, self.transmission)

coop = Base_Model(25000)
coop.info()

coop_blue = Base_Model(price=25500,color='blue')
coop_blue.info()

coop_manual_red = Base_Model(26000, 'Manual', 'Red')
coop_manual_red.info()

coop_manual_green = Base_Model(color='green', transmission='manual', price=26300)
coop_manual_green.info()

''' Demonstrate class definations '''
class Base_Model():
	''' Represent the base model of a car'''
	trim = 'normal'
	engine_liters = 1.5
	
	def engine_sound(self):
		return 'putt, putt'
	def horn_sound(self):
		retun 'beep, beep'
	def __str__(str):
		return 'Base Model'
coop = Base_Model()
print('%s has %s trim level.' % (coop, coop.trim))
print('%s has %s a %s liter engine.' % (coop, coop.engine_liters))
print('%s engine sounds like %s.' % (coop, coop.engine_sound()))
print('%s horn sounds like %s.' % (coop, coop.horn_sound()))



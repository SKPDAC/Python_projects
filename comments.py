''' Modules docstrings are a part of comments.

comments are documented in PEP 8.
'''

class Simple():
	''' Class docstrings should be included as comments. '''
	
	# Comments can be included at the same level of indentation.
	# Block comments start each line the same way.
	
	def __init__(self, value): # Inline comments share a line with code.
		''' Method docstrings are also important comments.'''
		self.value = value
		
		def double(self): # Avoid obvious comments
			''' Return double the initial value '''
			return 2 * self.value # Triple the value
			# Comments that confict with the code
			# are worse than no comments at all 
			
		def __mul__(self, value):
			''' implement the * Operator for self.value * value '''
			return self.value * value
		
		def __rmul__(self, value):
			''' implement the * operator for reversed operands '''
			return value * self.value
		
		def triple(value):
			''' Return three times the value '''
			return 3 * value
simple = Simple(10) # Create an instance of the Simple class
print ('Double the simple value is:', simple.double()) # double using method
print ('Triple the simple value is:', triple(simple)) # triple using the function
print ('Comments do not appear in the automatically generated help')
help(__name__)

			
			
			
			
			
			
			
			
			
			
			
			
	
# The while loop executes a suite of code if its condition is True
counter = 3
While counter > 0:
	print("Counting down:", counter)
	counter -= 1
While counter > 0:
	print('Never executes suite')
	print('when condition is false')
While 1:
	print('Executes at least once')
	if not counter:
	break
names = ['Tom', 'Ellen']
while names:
	print(names.pop(), 'is going')
	
results = [1, 0, 1]
processed = 0
passed = 0

while results:
	processed += 1
	result = results.pop()
	if not result:
	continue
	passed += 1
else:
	print('Procecssed:', processed, 'Passed:', passed)
	
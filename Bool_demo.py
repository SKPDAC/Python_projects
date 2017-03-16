# The only two instances of the boolean class are True or False
x = 1
print('bool(x) =', bool(x))
y = 0
print('bool(y) =', bool(y))
# The bool class is a subclass of 'int'
# Zero values are considered false, non-zero True
# Values considered false in Python
if not None: print('Non is false')
if not False: print('false is false')
if not (0 or 0.0 or oj): print('Zero is false')
if not ('' or [] or ()): print('Empty sequences are false')
if not ({} or set([])): print('Empty mappings are false')
# Boolean or returns first is True, or last false value
print('True or false returns', True or false)
print(('1 or 0 returns', 1 or 0)
print('None or 0 returns', None or 0)
# Booleaan and returns first False, or last true value
print('True and false returns', True and false)
print('1 and 0 returns', 1 and 0)
print('None and 0 returns', None and 0)
# Boolean Not returns False if operand is True
print('Not True returns', not true)
print('Not 1 returns', not 1)
print('Not "text" returns', not "text")
# boolean not returns true if operand is False
print('Not false returns', not false)
print('Not 0 returns', not 0)
print('Not "" returns', not "")

x, y = 5.0, 10
print('x =', x, ',', 'y =',y)
import math
# The math module provides a couple of constants
pi = math.pi
e = math.e
print('the value of pi is:', pi)
print('the ronded value of pi is:', rond(pi,4))
# The float class allows creation of special numbers
pos_inf = float('inf')
neg_inf = float('-inf')
not_a_num = float('nan')
# The math module provides functions to detect these numbers
print('math.isinf(pos_inf) =', math.isinf(pos_inf))
print('math.isinf(neg_inf) =', math.isinf(neg_inf))
print('math.isinf(not_a_num) =', math.isinf(not_a_num))
# Beware that these special numbers propagate with errors
Print('pos_inf * x =', pos_inf * x)
Print('neg_inf / y =', neg_inf / y)
print('pos_inf + neg_inf =', pos_inf + neg_inf)
print('not_a_num -y =', not_a_num - y)
#A nan value is never equal to another nan value
print('not_a_num == not_a_num =', not_a_num == not_a_num)
#The math module provides many other functions
print('math.factorial(5) =', math.factorial(5))
# logarithmic and power functions
print('math.log(x) =', math.log(x))
print('math.log10(x) =', math.log10(x))
print('math.exp(x) =', math.exp(x))
print('math.pow(x, x) =', math.pow(x, x))
print('math.sqrt(25) =', math.sqrt(25))
#Trigonometric fucntions
print('math.cos(x) =', math.cos(x))
print('math.acos(0.284) =', math.acos(0.284))
# Angular conversion functions
print('math.degrees(x) =', math.degrees(x))
print('math.radians(286.5) =', math.radians(286.5))
#Heperbolic functions
print('math.acosh(x) =', math.acosh(x))
print('math.asinh(x) =', math.asinh(x))










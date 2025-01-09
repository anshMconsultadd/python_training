x=2
y=5
z=7
# print(x+y+z)
# print(float(z))

# print(x,y,z)

# import math
# print(math.floor(-3.8))

import random
print(random.random())
print(random.randint(1,99))

setone={1,2,3}
settwo={2,3,4}
print(setone & settwo)
print(setone | settwo)
print(random.choice([1,2,3]))

z = 2 + 3j
print(z.real)  
print(z.imag)  

# Python provides built-in functions for numeric data:

# abs(x): Absolute value.
# round(x, n): Rounds a number to n decimal places.
# pow(x, y): Computes x**y.
# divmod(x, y): Returns a tuple (x // y, x % y).


from decimal import Decimal

x = Decimal('0.1') + Decimal('0.2')
print(x)  # Output: 0.3 (no floating-point rounding issues)




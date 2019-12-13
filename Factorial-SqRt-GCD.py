#------------------From Learning the Python 3 Standard Library------------------

#importing math functions
import math

#---------------------------Factorial and Square Root---------------------------
# Factorial of 3 = 3 * 2* 1
print('-----------Factorial of 3------------')
print(math.factorial(3))
# Squareroot of 64
print('------------Squareroot of 64----------')
print(math.sqrt(64))
# GCD-Greatest Common Denominator.  Useful for reducing fractions
# 8/52 = 2/13
# GCD between 8 and 52 is 4, so we can divide the numerator and denominator by 4
# to get a reduced fraction
print('------------Greatest Common Denominator of 52 and 8')
print(math.gcd(52, 8))
print(math.gcd(8, 52))

print(8/52)
print(2/13)

#-------------------------------Degrees and Radians-----------------------------
# In a full circle there are 360 degrees and 2 pi (6.28) radians in a circle
# At the 90 degree mark there are pi/2 radians
print('----------Degrees to Radians-----------') 
print (math.radians(360))
print(math.pi*2)
print('----------Radians to Degrees')
print(math.degrees(math.pi * 2))
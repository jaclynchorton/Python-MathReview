#--------------From Learning the Python 3 Standard Library-------------
#importing math module to give access to math functions
import math


#--------------------------------constants-----------------------------
# pi constant-The number π (/paɪ/) is a mathematical constant. Originally defined as 
# the ratio of a circle's circumference to its diameter, it now has various equivalent
# definitions and appears in many formulas in all areas of mathematics and physics. 
# It is approximately equal to 3.14159. It has been represented by the Greek letter "π"
# since the mid-18th century, though it is also sometimes spelled out as "pi". 
# It is also called Archimedes' constant.
print(math.pi)
#e constant--The number e is a mathematical constant that is the base of the natural 
# logarithm: the unique number whose natural logarithm is equal to one. It is 
# approximately equal to 2.71828,[1] and is the limit of (1 + 1/n)n as n approaches 
# infinity, an expression that arises in the study of compound interest. It can also 
# be calculated as the sum of the infinite series
print(math.e)

#-----------------------------Introduced in Python 3.5------------- 

#NAN-Not a defined number
print(math.nan)
#Infinity
print(math.inf)
#Negative Infinity
print(-math.inf)


#--------------------------------------Trigonometry-----------------

# cosine measures the adjacent side over the hypotenue of a triangle
#sine measures the opposite side over the hypotenuse
#At a 45 degree angle these are exactly the same

# So say we have a variable called obstacle direction here. And we're going to have it 
# be the value math dot cosine, math dot pi over four, which is that 45 degree angle 
# cosine value. 

#45 degree cosine value
obst_direction = math.cos(math.pi /4)
print('cosine') 
print(obst_direction)
#45 degree sine value
print('sine') 
print(math.sin(math.pi /4))

#-------------------------------------Ceiling and Floor--------------

cookies = 10.3
candy = 7
# Ceiling rounds up to the next whole number
print('cookies ceiling')
print (math.ceil(cookies))
print('candy ceiling') 
print (math.ceil(candy))

# Floor drops any remaining decimal value
age = 47.9
print('age floor')
print (math.floor(age))

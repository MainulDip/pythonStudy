'''
it is dockstring/multiline comments (for documentation)
'''

"""
variable name must starts with letters or underscores
"""

x = 1   # int
y = 2.5 # float
name = 'John' # str
booleanCheck = True # bool

# Multiple assaignment variables
a, b, check = (1, 'Hello', True)

print(a, b)


# Math and type and casting
a = x+y
print(type(a)) # <class 'float'>

stringConv = str(x)
intConvert = int(y)
intToFloat = float(intConvert)

print(type(stringConv), type(intConvert), type(intToFloat))
print(stringConv, intConvert, intToFloat) # 1 2 2.0


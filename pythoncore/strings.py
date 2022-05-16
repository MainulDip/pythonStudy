"""
Single or Double quote
"""
# Formating

from unicodedata import name


fname = "Hello"
lname = "world"

num = 77

s = 'some string'

print("Yooo, " + fname + " " + lname + " From Python and the number is " + str(num))

# String Formating By Position/placeholders
print('Formating testing {name} and {age}'.format(name=fname, age=num))

# F-String (Python 3.6+), can use both single and double  quote
print(f'F-String testing = {fname} and {lname}') 

# String Methods
print(lname.capitalize())


# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())
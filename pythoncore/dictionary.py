# A Dictionary is mutable, unordered, indexed collection. No Duplicate member is allowed
# Dictionary is like JSON in JS and hashes in Ruby

# Create dictionary
from pickle import POP

# dictionary create/define syntax
person = {
    'first_name' : 'John',
    'last_name' : 'Doe',
    'age' : 30
}

print(person, type(person))

# Contructor build
person2 = dict(first_name = 'William', last_name = "Smith", age = 27)
print(person2)

# Getting Value
print(person['first_name'], person['last_name'])

print(person2.get('last_name'))

# add key value
person['phone'] = '7777777777'

# get key
print(person.keys())
# get items
print(person.items())

# Copy
person3 = person.copy()
person3['city'] = 'Boston'

print(person3)

# Remove item
del(person3['age'])
person3.pop('last_name')
print(person3)

# Clear
person.clear()
print(person)

# Get length
print(len(person3))

# List/array of dictionary
people_list = [
    {'name': "Jonny", 'age': 30},
    {'name': "Nicola", 'age' : 47}
]

print(people_list[0]['name'])
# Tuple is orderd and immutable (unchangeable) collection/list/array. Allowes duplicate

# Create Tuple
fruits = ('apple', 'orange', 'grapes')
# Tuple using constructor
fruits2 = tuple(('banana', 'guava', 'papaya'))
print('Tuple printing : ', fruits, fruits2)

# need to add comma "," if tuple has single member. Without comma that will be string
fruits3 = ('WoodApple',)
fruits4 = ('BlueBerries')
print('single tuple with comma : ', fruits3, type(fruits3)) # ('WoodApple',) <class 'tuple'>
print('single tuple without comma : ', fruits4, type(fruits4)) # BlueBerries <class 'str'>


# getting value
print(fruits[1])

# Delete tuple
del fruits4
# print(fruits4) # will throw name error

# lenth
print("Tuple lenth : ", len(fruits))




# Set is mutable, unordered and unindexed collection. No Duplicate member is allowed
# Creating Set
fruits_set = {'apple', 'banana', 'mango', 'grape'}

# check if in set
print('Check if in set : ', 'apple' in fruits_set)

# adding
fruits_set.add('peers')

# No Duplicate
fruits_set.add('peers') # it will not throw an error but simply ignore adding

# removing
print("Before remove : ", fruits_set)
fruits_set.remove('grape')
print("After Remove : ", fruits_set)

# clear full set. it will make set empty
fruits_set.clear()
print("After clearing set : ", fruits_set)

# deleting full set, it will make it undefiened
del fruits_set
print(fruits_set) # will throw > NameError: name 'fruits_set' is not defined
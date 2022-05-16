# List is a collection which is ordered and mutable. Allows duplicate. Like array

num = [1,2,3,4]

# using constructor
num2 = list((1,3,5,7))
print(num, num2) # [1, 2, 3, 4] [1, 3, 5, 7]

fruits = ['apple', 'Orange', 'Grape', 'Guava']
print(fruits[1], len(fruits))

# appending
fruits.append('Lotkon')

# insert into exact position
fruits.insert(2, 'Strawberries')

# changing values
fruits[0] = "Blueberries"

# remove
fruits.remove('Guava')
print(fruits)

# remove with pop
fruits.pop(3)
print('Removing with pop : ', fruits)

# reverse
fruits.reverse()

# sort
fruits.sort()
fruits.sort(reverse=True)

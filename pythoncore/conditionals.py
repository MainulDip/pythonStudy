from re import X


x = 10
y = 4

# if elif else
if x > y:
    print(f'{x} is greater than {y}')
elif x < y:
    print(f'{x} is smaller than {y}')
else:
    if x < 0:
        print(f'{x} is negative')
    else:
        print(f'{x} and {y} is equal')

# Logical operators (and, or, not)
if x > 2 and x <= 10:
    print(f'something') 


# Membership operators (in, not in) => used to check if a sequence is presented in and object
numbers = [1.2,3,4,5,6,7]

if x in numbers:
    print(f'{x} is in {numbers}')
else:
    print(f'{x} is not in {numbers}')

# Identiry Operator (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with same memory location
if x is y:
    print(x is y)
elif x is not y:
    print(f'{x} and {y} are not equal')

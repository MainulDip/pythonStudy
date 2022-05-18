# No curly brackets, use indentation with tabs or space

# Create function
def sayHello(name, default = 'Yoo'):
    print(f'Hello {name} from {default}')

sayHello('World')

# Return values
def getSum(num1, num2):
    total = num1 + num2
    return total

print(getSum(4,3))


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow function or kotlin lambda
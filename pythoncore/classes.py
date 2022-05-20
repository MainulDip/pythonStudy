# Almost everything in python is an object

# Create class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.age = age
        self.email = email

    def greeting(self):
        return f'Name is {self.name}'

    def hello_world(self):
        return f'Hello World from {self.name}'



# initialize object
someone = User('John Doe', 'john@doe.com', 77)

print(someone.greeting())

print(someone.email)

print(type(someone))

# Extending Class
class Customer(User):
        # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.age = age
        self.email = email
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'Name is {self.name} and balance is {self.balance}'

# initialize customer

janet = Customer('Janet', 'janet@jonson.com', 76)
janet.set_balance(7777)
print(janet.greeting())

print(janet.hello_world())
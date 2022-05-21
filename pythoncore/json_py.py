# JSON into python dictionary parsing

from json import loads, dumps

userJSON = '{"first_name": "John", "last_name": "Doe", "age": 30}'

user = loads(userJSON) # parsing into python dictionary

print(user)

print(user['first_name'])


# dictionary to json
car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}
carJSON = dumps(car)
print(carJSON)
# a module is a file containing a set of functions to include in application.
# there are core python modules, modules installable using pip package manager
# including Django as well as custom modules


# importin core module
import datetime

today = datetime.date.today()
print(today)

from datetime import date
todayS = date.today()
print(todayS)

# External modules using pip
# pip install camelcase
# pip freeze or pip list => to show what package is installed
import camelcase
from camelcase import CamelCase
c = CamelCase()
print(c.hump('hello world')) # Hello World

# import custom module

import custommodule # or
from custommodule import validate_email

email = 'test@test.com'
if validate_email(email):
    print(f'{email} is valid')
else:
    print(f'{email} is invalid')
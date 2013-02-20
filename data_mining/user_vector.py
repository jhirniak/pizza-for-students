import random

# statics
toddler = 0; junior = 1; teen = 2; student = 3; adult = 4; senior = 5

user_example = { 'age' : student, 'active' : True, 'risk' : False, 'travel' : 5, 'friendly' : 5, 'exploration' : 5, 'nature' : 5, 'learning' : 5 }

from location import User
test_users = lambda how_many   : \
             [User( { 'age'         : random.randint(0,6), \
                 'sport'       : random.randint(0,10), \
                 'brave'       : random.randint(0,10), \
                 'travel'      : random.randint(0,10), \
                 'friendly'    : random.randint(0,10), \
                 'exploration' : random.randint(0,10), \
                 'nature'      : random.randint(0,10), \
                 'learning'    : random.randint(0,10) }) for x in range(how_many) ]

for t in test_users(20):
    print t

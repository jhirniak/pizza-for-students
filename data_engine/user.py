import random

# statics
toddler = 0; junior = 1; teen = 2; student = 3; adult = 4; senior = 5

class User:
    def __init__(self, preferences):
        self.profile = {'sport'       : 0,
                   'brave'       : 0,
                   'travel'      : 0,
                   'friendly'    : 0,
                   'exploration' : 0,
                   'nature'      : 0,
                   'learning'    : 0}
        for p in self.profile:
            self.profile[p] = preferences[p]

    def evaluate_location(self, location):
        return sum([ self.profile[p] * location.get_rating(p) for p in self.profile ])

    def println(self):
        print self.profile

# testing

user_example = { 'age' : student, 'active' : True, 'risk' : False, 'travel' : 5, 'friendly' : 5, 'exploration' : 5, 'nature' : 5, 'learning' : 5 }

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

import random
from world import Location
from data import Node

# statics
toddler = 0; junior = 1; teen = 2; student = 3; adult = 4; senior = 5

class User:
    def __init__(self, preferences, age):
        self.profile = {
            'sport'       : 0,
            'brave'       : 0,
            'travel'      : 0,
            'friendly'    : 0,
            'exploration' : 0,
            'nature'      : 0,
            'learning'    : 0
            }
        for p in self.profile:
            self.profile[p] = preferences[p]
        self.age = age

    def age(self):
        return self.age

    def rate(self, node):
        if isinstance(node, Node):
            location = node.data
        elif isinstance(node, Location):
            location = node
        else:
            return 0

        if (location.has_age_groups() and location.proper_age(self.age)) or not location.has_age_groups():
            return sum([ self.profile[p] * location.get_rating(p) for p in self.profile ])
        else:
            return 0
        
    # return list of locations 
    def rate_and_sort(self, locations):
        scored = []
        for l in locations:
            scored.append((self.rate(l), l))
        return sorted(scored, key=lambda (x, y) : x)[::-1]

    def println(self):
        print self.profile

# testing
# all int values from [0..8], total 9
user_example = { 'age' : student, 'sport' : True, 'brave' : False, 'travel' : 4, 'friendly' : 4, 'exploration' : 4, 'nature' : 4, 'learning' : 4 }
test_users = lambda how_many   : \
             [User( { 'sport'       : random.randint(0,10),
                      'brave'       : random.randint(0,10),
                      'travel'      : random.randint(0,10),
                      'friendly'    : random.randint(0,10),
                      'exploration' : random.randint(0,10),
                      'nature'      : random.randint(0,10),
                      'learning'    : random.randint(0,10) },
                      random.randint(0,6)) \
                  for x in range(how_many) ]

#for t in test_users(20):
#    print t

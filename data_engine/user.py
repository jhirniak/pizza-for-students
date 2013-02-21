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
<<<<<<< HEAD
            #print "__init__"

    def evaluate_location(self, location):
    #def rate(self, location):
    #print "evaluate_location"
        return sum([ self.profile[p] * location.get_rating(p) for p in self.profile ])
=======
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
>>>>>>> 0ca9024ce9be5832355743c5eba40fdbcefffddf

    def println(self):
        # print "println"
        print self.profile

# testing
# all int values from [0..8], total 9
user_example = { 'age' : student, 'sport' : True, 'brave' : False, 'travel' : 4, 'friendly' : 4, 'exploration' : 4, 'nature' : 4, 'learning' : 4 }
#print "ASD"
test_users = lambda how_many   : \
<<<<<<< HEAD
             [User( { 'age'         : random.randint(0,6), \
                 'sport'       : random.randint(0,10), \
                 'brave'       : random.randint(0,10), \
                 'travel'      : random.randint(0,10), \
                 'friendly'    : random.randint(0,10), \
                 'exploration' : random.randint(0,10), \
                 'nature'      : random.randint(0,10), \
                 'learning'    : random.randint(0,10) }) for x in range(how_many) ]
                 #print "DSA"
for t in test_users(20):
    #print "Debug"
    print t
    #print "End of module"
=======
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
>>>>>>> 0ca9024ce9be5832355743c5eba40fdbcefffddf

from user_vector import test_users
from label_data import data

import random
id = 0
for u in test_users(20):
    print "---"
    x = [ (u.evaluate_location(d), d.name) for d in data ]
    t = random.random() < 0.5
    x = sorted(x, key=lambda (x,y): x)[::-1][0 if t else 1:3 if t else 4]
    print "User ", id
    print x
    id += 1


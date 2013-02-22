from user import test_users
from label_data import data
import random
from query import *

id = 0
for u in test_users(20):
    print "---"
    u.println()
    #x = [ (u.rate(d), d.name) for d in data ]
    #t = random.random() < 0.5
    #x = sorted(x, key=lambda (x,y): x)[::-1][0 if t else 1:3 if t else 4]
    #x = sorted(x, key=lambda (x,y): x)[::-1][0:3]
    #x = u.rate_and_sort(data)
    #x = get_them_all_scored(u)
    x = any_2_dict(get_them_all())
    print "User ", id
    print x
    id += 1

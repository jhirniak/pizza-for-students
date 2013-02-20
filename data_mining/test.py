from user_vector import test_users
from label_data import data

for u in test_users(20):
    print "---"
    for d in data:
        x = u.evaluate_location(d)
        if x > 0:
            print x


# example usage at the bottom

from data import tree # kd tree ballanced around location data
from geometry import Infinity, Circle

# some age_groups and features items got mixed, I think it is because of wrong
# mapping set-up in the batch program
# nothing to do with yours part, but just wanted to let know if one result seems
# out of place (mapping is done in label_data.py)

# for result as a dictionary use any_2_dict(_other_method_)
# ex. any_2_dict(get_them_all())
def any_2_dict(x):
    if isinstance(x[0], tuple):
        return [ data[1].data.__dict__ for data in x ]
    else:
        return [ t.data.__dict__ for t in x ]

# creates output for map
def get_for_map(x, accepted_fields):
    return [ xs for xs in x if xs in accepted_fields ]

# returns dictionary with 3 fields:
# . 'location'    : (longitude, latitude)
# . 'name'        : name
# . 'type'        : type (e.g. Museum, Gallery, Park etc.)
# . 'description' : description
def get_for_map_summary(x):
    accepted_fields = ['location', 'name', 'type', 'description']
    return get_for_map(x, accepted_fields)

def get_them_all():
    return tree.in_area(Infinity())

# centre should be point Point(longitude, latitude) or in easy peasy saying Point(x, y)
def get_in_radius(centre, radius):
    return tree.in_area(Circle(centre, radius))

# user is instance of User, which class is in user.py
def get_them_all_scored(user):
    return user.rate_and_sort(get_them_all())

def get_in_radius_scored(user, centre, radius):
    return user.rate_and_sort(get_in_radius(centre, radius))

def get_top_n(n, user):
    return get_them_all_scored(user)[0:n]

def get_top_n_in_radius(n, user, centre, radius):
    return get_in_radius_scored(user, centre, radius)[0:n]

def get_top_10(user):
    return get_top_n(10, user)

def get_top_10_in_radius(user, centre, radius):
    return get_top_n_in_radius(10, user, centre, radius)

def get_top_3(user):
    return get_top_n(3, user)

def get_top_3_in_radius(user, centre, radius):
    return get_top_n_in_radius(3, user, centre, radius)

def get_top_3_in_radius_2_dict(user, centre, radius):
    return [ t.data.__dict__ for t in get_top_3_in_radius(user, centre, radius) ]

# example usage
from user import test_users

for u in test_users(1):
    print any_2_dict(get_top_3(u))

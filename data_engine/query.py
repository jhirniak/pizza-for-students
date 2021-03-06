# example usage at the bottom

from data import tree # kd tree ballanced around location data
from geometry import Infinity, Circle
from labels import types

# some age_groups and features items got mixed, I think it is because of wrong
# mapping set-up in the batch program
# nothing to do with yours part, but just wanted to let know if one result seems
# out of place (mapping is done in label_data.py)

# for result as a dictionary use any_2_dict(_other_method_)
# ex. any_2_dict(get_them_all())
def any_2_dict(x):
    if x in [None, []]:
        return {}
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

def good_weather(user, centre, radius):
    return any_2_dict([ y for (x, y) in (get_top_10_in_radius(user, centre, radius)) ])
    
def bad_weather(user, centre, radius):
    locs = [ y.data for (x,y) in get_in_radius_scored(u, Point(51.0, -3.0), 100.0) ]
    indoors = []
    for l in locs:
        if not l.outdoor:
            indoors.append(l)
            if len(indoors) > 9:
                break
    return [ i.__dict__ for i in indoors ]

def get_singleton_connected(all_points):
    connectable = ['Museum', 'History', 'Play Area', 'Park']

    connected  = [ p for p in all_points if p['type'] in connectable ]
    singletons = [ p for p in all_points if p['type'] not in connectable ]
    return (singletons, connected)

def count_types(data):
    counts = { t : 0 for t in types }
    for d in data:
        counts[d['type']] += 1
    return counts
        

def ulli_data(data):
    if data in [None, ""]:
        return ""
    ulli = "<ul>"
    for li in ulli:
        ulli += "<li>" + li + "</li>"
    ulli += "</ul>"                

def generate_bottom(data):
    bottom = ""
    for d in data:
        bottom += "<h1>" + d['name'] + "</h1>"
        if 'description' in d and d['description']:
            bottom += "<h2>Description:</h2><p>" + d['description'] + "</p>"
        if 'features' in d.keys():
            bottom += "<h2>Features</h2>"
            bottom += ulli_data(d['features'])
        if 'activities' in d.keys():
            bottom += "<h2>Activities:</h2>"
            bottom += ulli_data(d['activities'])
    return bottom

# example usage
from user import test_users
from geometry import Point

print "\n\n\n\n\n\n\n\n\n\n"
for u in test_users(1):
    # get bad weather
    bad = bad_weather(u, Point(51.0, -3.0), 1000.0)
    bad_4_map = get_singleton_connected(bad_weather(u, Point(51.0, -3.0), 1000.0))
    print len(bad_4_map[0]) + len(bad_4_map[1])
    print bad_4_map
    print "\n\n---\n\n"
    # get good weather
    good = good_weather(u, Point(51.0, -3.0), 1000.0)
    good_4_map = get_singleton_connected(good_weather(u, Point(51.0, -3.0), 1000.0))
    print len(good_4_map[0]) + len(good_4_map[1])
    print good_4_map
    print "\n\n---\n\n"
    # count types
    print count_types(bad)
    print count_types(good)
    # print bottom for website
    print "\n\n---\n\n"
    print generate_bottom(bad)
    print "\n\n...\n\n"
    print generate_bottom(good)
    #print [ y for (x,y) in get_in_radius_scored(u, Point(51.0, -3.0), 100.0) ]
#    print get_10_to_map(u, Point(51.0, -3.0), 7.5)
    #x= any_2_dict(get_top_10(u))[2]
    #print x['feature']
    """print any_2_dict(get_top_10(u))
    for x in any_2_dict(get_top_10(u)):
        if 'features' in x.keys():
            print x['features']
    """
    #print generate_bottom(any_2_dict(get_top_10(u)))

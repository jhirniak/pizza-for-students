class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def add(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def midpoint(self, other):
        return Point((self.x + other.x) / 2.0, (self.y + other.y) / 2.0)

    def in_radius_distance(self, centre, radius):
        return self.distance(centre) <= radius

class Area:
    def __init__(self, convex):
        self.convex = convex

    def centre(self):
        common = [self.convex[i].x * self.convex[i+1].y \
                  - self.convex[i+1] * self.convex[i].y \
                  for i in range(len(self.convex))]
        area = 0.5 * sum(common)
        x = 1.0 / 6.0 / area * sum([ (self.convex[i].x + self.convex[i+1].x) * common[i] \
                                      for i in range(len(self.convex)) ])
        y = 1.0 / 6.0 / area * sum([ (self.convex[i].y + self.convex[i+1].y) * common[i] \
                                      for i in range(len(self.convex)) ])
        return Point(x, y)

    def within(self, point):
        pass

from labels import bools

class Rating:
    def __init__(self, valid=[]):
        # print valid
        self.rating = { b : False for b in bools }
        for v in valid:
            self.rating[v] = True
        #print self.rating

    def get_rating(self, label):
        if label in self.rating:
            return self.rating[label]
        else:
            return False

    def add_rating(self, label, rating=None):
        if label in self.rating:
            self.rating[label] = value
        else:
            self.rating.update({label : value})

    def remove_rating(self, label):
        del self.rating[label]

    def get_keys(self):
        return self.rating.keys()

    def get_ratings(self):
        return self.rating

    def get_vector(self):
        return [ y for (x, y) in self.rating.items() ]

    def get_annotated_vector(self):
        return self.rating.items()

class Feature:
    def __init__(self, features=[]):
        self.feature = features

    def add_feature(self, feature):
        if isinstance(feature, list):
            for f in feature:
                self.feature.append(f)
        else:
            self.feature.append(feature)
    def remove_feature(self, feature):
        del self.feature[self.feature.index(feature)]

    def get_features(self):
        return self.feature

    def contains(self, feature):
        return feature in self.feature

class Description:
    def __init__(self, description=''):
        self.description = description
    
class Location(Point, Rating, Feature, Description):
    def __init__(self, location, cat, name, rating=[], feature=[], description=''):
        Point.__init__(self, location.x, location.y)
        self.name = name
        self.type = cat
        Rating.__init__(self, rating)
        Feature.__init__(self, feature)
        Description.__init__(self, description)

    def latitude(self):
        return self.x

    def longitude(self):
        return self.y

class Place(Area, Rating, Feature, Description):
    def __init__(self, name, convex, feature=[]):
        self.name = name
        Area.__init__(self, convex)
        Feature.__init__(self, feature)

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

from geometry import Point, Area
from labels import bools

class Rating:
    def __init__(self, valid=[], age_groups=[]):
        self.rating = { b : False for b in bools }
        for v in valid:
            self.rating[v] = True
        self.age_groups = age_groups

    def get_rating(self, label):
        return self.rating[label]
        
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
    def __init__(self, location, cat='', name='', rating=[], age_groups=[], feature=[], description=''):
        Point.__init__(self, location.x, location.y)
        self.geo = (self.x, self.y) # redundant, but may be useful for Kuba
        self.name = name
        self.type = cat
        Rating.__init__(self, rating)
        self.age_groups = age_groups
        Feature.__init__(self, feature)
        Description.__init__(self, description)

    def latitude(self):
        return self.x

    def longitude(self):
        return self.y

    def add_rating(self, score):
        self.rating = score

    def has_age_groups(self):
        return len(self.age_groups) > 0

    def proper_age(self, age):
        return age in self.age_groups

class Place(Area, Rating, Feature, Description):
    def __init__(self, name, convex, feature=[]):
        self.name = name
        Area.__init__(self, convex)
        Feature.__init__(self, feature)

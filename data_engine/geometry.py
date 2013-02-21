class Point:
    def __init__(self, x, y):
        self.x, self.y = float(x), float(y)

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def add(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def midpoint(self, other):
        return Point((self.x + other.x) / 2.0, (self.y + other.y) / 2.0)

    def in_radius_distance(self, centre, radius):
        return self.distance(centre) <= radius

    def location(self):
        return Point(self.x, self.y)

class Square:
    def __init__(self, p0, p1):
        self.xmin = min([p0.x, p1.x])
        self.xmax = max([p0.x, p1.x])
        self.ymin = min([p0.y, p1.y])
        self.ymax = max([p0.y, p1.y])
    
    def contains(self, point):
        return self.xmin <= point.x and point.x <= self.xmax \
           and self.ymin <= point.y and point.y <= self.ymax

class Circle:
    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius

    def contains(self, point):
        return self.centre.distance(point) <= self.radius

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

    def contains(self, point):
        pass

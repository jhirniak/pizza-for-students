from geometry import Point, Square, Circle

class Node: pass

class KDtree:
    def __init__(self, nodes, key):
        self.root = kdtree(nodes, key)

    def in_square(self, boundary):
        return between(boundary, self.root)

    def in_radius(self, centre, radius):
        pass

def between(boundary, node):
        
    if not node:
        return []

    if boundary.contains(node.location()):
        return [node] + between(boundary, node.left_child) + between(boundary, node.right_child)
    else:
        return []

location_key = lambda obj : list([obj.x, obj.y])

def kdtree(nodes, key, depth=0):
 
    if not nodes:
        return None
 
    # Select axis based on depth so that axis cycles through all valid values
    k = len(key(nodes[0])) # assumes all points have the same dimension
    axis = depth % k
 
    # Sort point list and choose median as pivot element
    sorted(nodes, key=lambda d : key(d)[axis])
    median = len(nodes) // 2 # choose median
 
    # Create node and construct subtrees
    node = Node()
    node.location = nodes[median].location
    node.data = nodes[median]
    node.left_child = kdtree(nodes[:median], key, depth + 1)
    node.right_child = kdtree(nodes[median + 1:], key, depth + 1)
    return node

# test

from label_data import data

tree = KDtree(data, location_key)
print len(tree.in_square(Square(Point(45.0,-5.0), Point(55.99,5.0))))
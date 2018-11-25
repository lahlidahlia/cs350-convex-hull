import numpy as np

# Takes in the list of points, and returns the point
# furthest on the left side.
def left_most_point(points):
    leftMost = []
    for point in points:
        if not leftMost or point[0] < leftMost[0]:
            leftMost = list(point)
    return leftMost

# Takes in the list of points, and returns the points
# furthest on the left and right sides as a tuple.
def lr_most_point(points):
    leftMost  = []
    rightMost = []
    for point in points:
        if not leftMost or point[0] < leftMost[0]:
            leftMost = list(point)
        if not rightMost or point[0] > rightMost[0]:
            rightMost = list(point)
    return (leftMost, rightMost)

# Returns the shortest distance between the point C,
# and the line segment connected by P and Q.
def dist(P, Q, C):
    A = np.subtract(P, C)
    B = np.subtract(P, Q)
    magB = np.linalg.norm(B)

    proj = (np.dot(A, B) / (magB*magB)) * B
    return np.linalg.norm(np.subtract(A, proj))

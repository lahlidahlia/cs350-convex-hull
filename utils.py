import numpy as np

# Takes in the array of points, and returns the point
# furthest on the left side.
def left_most_point(points):
    leftMost = np.array([])
    N = len(points)
    for i in range(N):
        if leftMost.size == 0 or points[i][0] < leftMost[0]:
            leftMost = points[i]
    return leftMost

# Takes in the array of points, and returns the points
# furthest on the left and right sides as a tuple.
def lr_most_point(points):
    leftMost = np.array([])
    rightMost = np.array([])
    N = len(points)
    for i in range(N):
        if leftMost.size == 0 or points[i][0] < leftMost[0]:
            leftMost = points[i]
        if rightMost.size == 0 or points[i][0] > rightMost[0]:
            rightMost = points[i]
    return (leftMost, rightMost)

# Returns the distance between the point C,
# and the line segment connected by P and Q.
def dist(P, Q, C):
    A = np.subtract(P, C)
    B = np.subtract(P, Q)
    magB = np.linalg.norm(B)

    proj = (np.dot(A, B) / (magB*magB)) * B
    return np.linalg.norm(np.subtract(A, proj))

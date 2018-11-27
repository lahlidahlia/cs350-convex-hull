import numpy as np

def left_most_point(points):
    '''
    Takes in the list of points, and returns the point
    furthest on the left side.
    '''
    leftMost = []
    for point in points:
        if not leftMost or point[0] < leftMost[0]:
            leftMost = list(point)
    return leftMost

def lr_most_point(points):
    '''
    Takes in the list of points, and returns the points
    furthest on the left and right sides as a tuple.
    '''
    leftMost  = []
    rightMost = []
    for point in points:
        if not leftMost or point[0] < leftMost[0]:
            leftMost = list(point)
        if not rightMost or point[0] > rightMost[0]:
            rightMost = list(point)
    return (leftMost, rightMost)

def dist(P, Q, C):
    '''
    Returns the shortest distance between the point C,
    and the line segment connected by P and Q.
    '''
    A = np.subtract(P, C)
    B = np.subtract(P, Q)
    magB = np.linalg.norm(B)

    proj = (np.dot(A, B) / (magB*magB)) * B
    return np.linalg.norm(np.subtract(A, proj))


def sort_by_x(points):
    '''
    Sort the array by x coordinate, or by y coordinate in case of tie.
    Returns a array of data points. (Does not modify the array)
    '''
    indices = np.lexsort((points[:,1], points[:,0]))
    return points[indices]
   

def cross(a, b, o):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1]  - o[1]) * (b[0] - o[0])

import numpy as np

def left_most_point(points):
    '''
    Takes in the array of points, and returns the point
    furthest on the left side.
    '''
    leftMost = np.array([])
    for point in points:
        if leftMost.size == 0 or point[0] < leftMost[0]:
            leftMost = point
    return leftMost

def lr_most_point(points):
    '''
    Takes in the array of points, and returns the points
    furthest on the left and right sides as a tuple.
    '''
    leftMost  = np.array([])
    rightMost = np.array([])
    for point in points:
        if leftMost.size == 0 or point[0] < leftMost[0]:
            leftMost = point
        if rightMost.size == 0 or point[0] > rightMost[0]:
            rightMost = point
    return (leftMost, rightMost)

def dist(A, B, C):
    '''
    Returns the shortest distance between the point C,
    and the line segment connected by A and B.
    '''
    P = A - C
    Q = A - B
    magQ = np.linalg.norm(Q)

    proj = (np.dot(P, Q) / (magQ*magQ)) * Q
    return np.linalg.norm(P - proj)


def sort_by_x(points):
    '''
    Sort the array by x coordinate, or by y coordinate in case of tie.
    Returns a array of data points. (Does not modify the array)
    '''
    indices = np.lexsort((points[:,1], points[:,0]))
    return points[indices]
   

def cross(a, b, o):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1]  - o[1]) * (b[0] - o[0])

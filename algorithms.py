import utils
import numpy as np

# Gift Wrapping algorithm that takes in the array of
# points.
# Returns the convex hull as a list of arrays.
def gift_wrap(points):
    result = []
    pointOnHull = utils.left_most_point(points)
    N = len(points)

    endPoint = np.array([])
    i = 0
    while True:
        result.append(pointOnHull)
        endPoint = points[0]
        oldLine = np.subtract(endPoint,  result[i])
        for j in range(1, N):
            newLine = np.subtract(points[j], result[i])
           
            if (endPoint == pointOnHull).all() \
                    or np.cross(newLine, oldLine) < 0:
                endPoint = points[j]
                oldLine = np.subtract(endPoint,  result[i])

        i += 1
        pointOnHull = endPoint

        if (endPoint == result[0]).all():
            break

    return result

# Quick Hull algorithm that takes in the array of
# points.
# Returns the convex hull as a list a list of arrays.
def quick_hull(points):
    A, B = utils.lr_most_point(points)
    result = []
    result.append(A)
    result.append(B)

    S1 = []
    S2 = []
    N = len(points)
    oldLine = np.subtract(result[0], result[1])
    for i in range(N):
        newLine = np.subtract(result[0], points[i])
        if np.cross(oldLine, newLine) > 0:
            S1.append(points[i])
        elif (points[i] != result[0]).all() \
                and (points[i] != result[1]).all():
            S2.append(points[i])

    find_hull(S1, result[0], result[1], 1, result)
    find_hull(S2, result[-1], result[0], len(result), result)

    return result

# Recursive function for  the Quick Hull algorithm
# that takes in the set of points to the right of the
# line between P and Q.  Additionally, takes in the
# index of the next point and the list of results.
# Returns a list a list of arrays.
def find_hull(Sk, P, Q, index, result):
    if not Sk:
        return []

    S1 = []
    S2 = []
    C = np.array([])
    dist_C = 0
    for point in Sk:
        dist_Point = utils.dist(P, Q, point)
        if dist_C < dist_Point:
            C = point
            dist_C = dist_Point

    result.insert(index, C)
    PtoC = np.subtract(P, C)
    CtoQ = np.subtract(C, Q)
    for point in Sk:
        CtoPoint = np.subtract(C, point)
        if np.cross(PtoC, CtoPoint)   > 0:
            S1.append(point)
        elif np.cross(CtoQ, CtoPoint) > 0:
            S2.append(point)

    orig_len = len(result)
    find_hull(S1, P, C, index, result)
    next_index = len(result) - orig_len + index + 1
    find_hull(S2, C, Q, next_index, result)

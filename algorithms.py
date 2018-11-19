import utils
import numpy as np

# Gift Wrapping algorithm that takes in the array of
# points and the list of lines that are to be displayed.
# Returns the convex hull as a regular python list.
def gift_wrap(points):
    result = []
    pointOnHull = utils.left_most_point(points)
    N = len(points)

    endPoint = []
    i = 0
    while True:
        result.append(np.array(pointOnHull))
        endPoint = list(points[0])
        for j in range(1, N):
            oldLine = np.subtract(endPoint,  result[i])
            newLine = np.subtract(points[j], result[i])
           
            if endPoint == pointOnHull or np.cross(newLine, oldLine) < 0:
                endPoint = list(points[j])
        i += 1
        pointOnHull = endPoint

        if endPoint == list(result[0]):
            break

    return np.array(result).tolist()

from sys import argv
import numpy as np
import matplotlib.pyplot as plt

# Properties of the points
p_color = 'r'
p_area  = 20
p_alpha = 0.75

# Properties of the lines
l_color = 'b'
l_alpha = 0.5

# Takes in the array of points, and returns the point
# furthest on the left-side.
def left_most_point(points):
    leftMost = []
    N = len(points)
    for i in range(N):
        if not leftMost or points[i][0] < leftMost[0]:
            leftMost = list(points[i])
    return leftMost

# Gift Wrapping algorithm that takes in the array of
# points and the list of lines that are to be displayed.
# Returns the convex hull as a 2D array
def gift_wrap(points, lines):
    result = []
    pointOnHull = left_most_point(points)
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
        elif '-v' in argv:
            x, y = np.array(result).T
            if lines:
                lines.pop(0).remove()
            lines = plt.plot(x, y, c=l_color, alpha=l_alpha)
            plt.pause(0.001)

    result = np.array(result)

    if '-v' in argv:
        x, y = np.vstack((result, result[0])).T
        if lines:
            lines.pop(0).remove()
        lines = plt.plot(x, y, c=l_color, alpha=l_alpha)
        plt.pause(0.001)

    return result

if __name__ == '__main__':
    points = np.random.rand(10, 2)
    lines = []

    if '-v' in argv:
        x, y = points.T
        plt.scatter(x, y, s=p_area, c=p_color, alpha=p_alpha)

        # Gift Wrapping algorithm plot
        plt.title('Gift Wrapping')
        plt.xlabel('X')
        plt.ylabel('Y')

    print("Gift Wrap results:")
    print(gift_wrap(points, lines))

    # if '-v' in argv:
         #Quick Hull algorithm plot
    #     if lines:
    #         lines.pop(0).remove()
    #     plt.title('Quick Hull')

    # TODO: implement quick_hull(points)

    if '-v' in argv:
        plt.show()

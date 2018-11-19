from local import *
import matplotlib.pyplot as plt

# Takes in the array of points, and returns the point
# furthest on the left side.
def left_most_point(points):
    leftMost = []
    N = len(points)
    for i in range(N):
        if not leftMost or points[i][0] < leftMost[0]:
            leftMost = list(points[i])
    return leftMost

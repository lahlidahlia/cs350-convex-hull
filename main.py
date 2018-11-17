import time
import numpy as np
import matplotlib.pyplot as plt
from sys import argv

# Number of generated points
N = 500
# Delay between frames
visual_delay = 0.0001

# Properties of the points
p_color = 'r'
p_area  = 20
p_alpha = 0.5

# Properties of the lines
l_color = 'b'
l_alpha = 0.75

# Visual components
timer = 0
lines = []

# Plots connected lines based on the provided points.
# Displays a timer based on the provided start time.
# Saves a `.png` file of the current frame
def draw_lines(points, start_time, file_name):
    global lines, timer
    x, y = points.T
    if lines:
        lines.pop(0).remove()
    lines = plt.plot(x, y, c=l_color, alpha=l_alpha)
    timer.set_text("%.2f sec" % (time.time() - start_time))
    plt.savefig('frames/' + file_name + '.png')
    plt.pause(visual_delay)

# Takes in the array of points, and returns the point
# furthest on the left side.
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
def gift_wrap(points, start_time):
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
        elif visual:
            draw_lines(np.array(result), start_time, str(i))

    result = np.array(result)

    if visual:
        draw_lines(np.vstack((result, result[0])), start_time, str(i))

    return result

if __name__ == '__main__':
    points = np.random.rand(N, 2)
    visual = False
    if '-v' in argv:
        visual = True

    if visual:
        x, y = points.T
        plt.scatter(x, y, s=p_area, c=p_color, alpha=p_alpha)
        plt.xlabel('X')
        plt.ylabel('Y')

        plt.title('Gift Wrapping')
        timer = plt.text(0, 1, "0.0 sec")

    start_time = time.time()
    print("Gift Wrap results:\n" + str(gift_wrap(points, start_time)))
    print("Solved in %.2f seconds" % (time.time() - start_time))

    # if visual:
    #     if lines:
    #         lines.pop(0).remove()
    #     plt.title('Quick Hull')
    #     timer = plt.text(0, 1, "0.0 sec")

    # TODO: implement quick_hull(points)

    if visual:
        plt.show()

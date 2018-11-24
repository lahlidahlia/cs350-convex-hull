import utils
import numpy as np
import config
import matplotlib.pyplot as plt
import time

# The initialization function for the plot.
def init_plot(points):
    x, y = points.T
    plt.scatter(x, y, s=config.p_area, c=config.p_color,
            alpha=config.p_alpha)
    plt.xlabel('X')
    plt.ylabel('Y')
    config.timer = plt.text(0.9, 1, "")

# The function to reset the plot.
def reset_plot(title):
    if config.lines:
        config.lines.pop(0).remove()
    config.timer.set_text("0.0 sec")
    plt.title(title)

# Plots connected lines based on the provided points.
# Displays a timer based on the provided start time.
# Saves a `.png` file of the current frame
def draw(file_name, start_time):
    plt.legend(loc=2)
    config.timer.set_text("%.2f sec" % (time.time() - start_time))
    plt.savefig('frames/' + file_name + '.png')
    plt.pause(config.visual_delay)

# Gift Wrapping algorithm that takes in the array of
# points and start time of the timer.
# Returns the convex hull as a list of arrays.
def draw_gift_wrap(points, start_time):
    result = []
    pointOnHull = utils.left_most_point(points)

    next_guess = []
    c_x = [pointOnHull[0]]
    c_y = [pointOnHull[1]]

    N = len(points)
    endPoint = np.array([])
    i = 0
    while True:
        result.append(pointOnHull)
        endPoint = points[0]
        oldLine = np.subtract(endPoint,  result[i])

        x, y = np.vstack((endPoint,  result[i])).T
        if next_guess:
            next_guess.pop(0).remove()
        next_guess = plt.plot(x, y, c=config.n_color,
                alpha=config.n_alpha, label='Next Best')
        draw(str(i) + '_0', start_time)
        for j in range(1, N):
            newLine = np.subtract(points[j], result[i])
           
            if (endPoint == pointOnHull).all() \
                    or np.cross(newLine, oldLine) < 0:
                endPoint = points[j]
                oldLine = np.subtract(endPoint,  result[i])
                x, y = np.vstack((endPoint,  result[i])).T
                next_guess.pop(0).remove()
                next_guess = plt.plot(x, y, c=config.n_color,
                        alpha=config.n_alpha, label='Next Best')
                draw(str(i) + '_' + str(j), start_time)

        if config.lines:
            config.lines.pop(0).remove()
            c_x.append(x[1])
            c_y.append(y[1])
        c_x.append(endPoint[0])
        c_y.append(endPoint[1])

        config.lines = plt.plot(c_x, c_y, c=config.c_color,
                alpha=config.c_alpha, label='Convex')

        i += 1
        pointOnHull = endPoint

        if (endPoint == result[0]).all():
            break

    next_guess.pop(0).remove()
    draw('final', start_time)
    return result

# Quick Hull algorithm that takes in the array of
# points, and the start time of the timer.
# Returns the convex hull as a list.
def draw_quick_hull(points, start_time):
    A, B = utils.lr_most_point(points)
    result = []
    result.append(A)
    result.append(B)

    x, y = np.vstack((A, B)).T
    config.lines = plt.plot(x, y, c=config.c_color, alpha=config.c_alpha,
            label='Convex')
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

    draw_find_hull(S1, result[0], result[1], 1, result, start_time)
    draw_find_hull(S2, result[-1], result[0], len(result), result, start_time)
    draw('final', start_time)

    return result

# Recursive function for  the Quick Hull algorithm
# that takes in the set of points to the right of the
# line between P and Q.  Additionally, takes in the
# index of the next point, the list of results, and
# the start time of the timer.
# Returns a list a list of arrays.
def draw_find_hull(Sk, P, Q, index, result, start_time):
    if not Sk:
        return []

    next_guess = []

    S1 = []
    S2 = []
    C = np.array([])
    dist_C = 0
    for point in Sk:
        dist_Point = utils.dist(P, Q, point)
        if dist_C < dist_Point:
            if next_guess:
                next_guess.pop(0).remove()
            x = y = 0
            if index == len(result):
                x, y = np.vstack((result[-1], point, result[0])).T
            else:
                x, y = np.vstack((result[index - 1], point,
                        result[index])).T
            next_guess = plt.plot(x, y, c=config.n_color,
                    alpha=config.n_alpha, label='Next Best')
            draw('div', start_time)
            C = point
            dist_C = dist_Point

    result.insert(index, C)
    next_guess.pop(0).remove()
    config.lines.pop(0).remove()
    x, y = np.vstack((result, result[0])).T
    config.lines = plt.plot(x, y, c=config.c_color,
            alpha=config.c_alpha, label='Convex')

    PtoC = np.subtract(P, C)
    CtoQ = np.subtract(C, Q)
    for point in Sk:
        CtoPoint = np.subtract(C, point)
        if np.cross(PtoC, CtoPoint)   > 0:
            S1.append(point)
        elif np.cross(CtoQ, CtoPoint) > 0:
            S2.append(point)

    orig_len = len(result)
    draw_find_hull(S1, P, C, index, result, start_time)
    next_index = len(result) - orig_len + index + 1
    draw_find_hull(S2, C, Q, next_index, result, start_time)

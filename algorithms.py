import utils
import config
import numpy as np
import matplotlib.pyplot as plt
from draw import draw
from pprint import pprint

def brute_force(points, start_time):
    '''
    Brute Force algorithm that takes in the array of
    points and start time of the timer.
    Returns the convex hull as an array.
    The results of this algorithm are out-of-order,
    unlike the other algorithms that have their results in-order.
    '''
    result = []
    lines = []
    if config.visual:
        lines.append(config.ax.plot((0,0), (0,0), c=config.c_color,
                alpha=config.c_alpha, label=config.c_label))
    for i in points:
        for j in points:
            if (i == j).all():
                continue
            side = 0
            ItoJ = j - i
            for k in points:
                if (i == k).all() or (j == k).all():
                    continue
                ItoK = i - k
                newSide = np.cross(ItoJ, ItoK)
                if newSide != 0:# Makes sure the three lines are not collinear
                    if side == 0:
                        side = newSide
                    elif (side < 0 and newSide > 0) or \
                         (side > 0 and newSide < 0):
                        side = False
                        break
            if side:
                i_is_new = all(i not in q for q in result)
                j_is_new = all(j not in q for q in result)
                if i_is_new or j_is_new:
                    if i_is_new:
                        result.append(i)
                    if j_is_new:
                        result.append(j)
                    if config.visual:
                        lines.append(config.ax.plot(
                                (i[0], j[0]), (i[1], j[1]),
                                color=config.c_color, alpha=config.c_alpha))
                        draw(start_time)
                elif config.visual: # TODO: This happens too many times
                    lines.append(config.ax.plot(
                            (i[0], j[0]), (i[1], j[1]),
                            color=config.c_color, alpha=config.c_alpha))
                    draw(start_time)

    if config.visual:
        plt.savefig(config.image_path)
        for line in lines:
            line.pop(0).remove()
    return np.array(result)

def gift_wrap(points, start_time):
    '''
    Gift Wrapping algorithm that takes in the array of
    points and start time of the timer.
    Returns the convex hull as an array.
    '''
    if points.size == 0:
        return []

    result = []
    pointOnHull = utils.left_most_point(points)

    next_guess = []
    c_x = [pointOnHull[0]]
    c_y = [pointOnHull[1]]

    N = len(points)
    endPoint = np.array([])
    while True:
        result.append(pointOnHull)
        endPoint = points[0]
        oldLine = endPoint - result[-1]

        if config.visual:
            x, y = np.vstack((endPoint,  result[-1])).T
            if next_guess:
                next_guess.pop(0).remove()
            next_guess = config.ax.plot(x, y, c=config.n_color,
                    alpha=config.n_alpha, label=config.n_label)
            draw(start_time)
        for j in range(1, N):
            newLine = points[j] - result[-1]
           
            if (endPoint == pointOnHull).all() \
                    or np.cross(newLine, oldLine) < 0:
                endPoint = points[j]
                oldLine = endPoint - result[-1]
                if config.visual:
                    x, y = np.vstack((endPoint,  result[-1])).T
                    next_guess.pop(0).remove()
                    next_guess = config.ax.plot(x, y, c=config.n_color,
                            alpha=config.n_alpha, label=config.n_label)
                    draw(start_time)

        if config.visual:
            if config.lines:
                config.lines.pop(0).remove()
                c_x.append(x[1])
                c_y.append(y[1])
            c_x.append(endPoint[0])
            c_y.append(endPoint[1])

            config.lines = config.ax.plot(c_x, c_y, c=config.c_color,
                    alpha=config.c_alpha, label=config.c_label)

        pointOnHull = endPoint

        if (endPoint == result[0]).all():
            break
    
    if config.visual:
        next_guess.pop(0).remove()
        draw(start_time)
        plt.savefig(config.image_path)
    return np.array(result)

def quickhull(points, start_time):
    '''
    Quickhll algorithm that takes in the array of
    points, and the start time of the timer.
    Returns the convex hull as an array.
    '''
    if points.size == 0:
        return []

    L, R = utils.lr_most_point(points)
    result = [L, R]
    if config.visual:
        x, y = np.vstack((L, R)).T
        config.lines = config.ax.plot(x, y, c=config.c_color,
                alpha=config.c_alpha, label=config.c_label)
    S1 = []
    S2 = []
    oldLine = L - R
    for point in points:
        newLine = L - point
        if np.cross(oldLine, newLine) > 0:
            S1.append(point)
        elif (point != L).all() and (point != R).all():
            S2.append(point)

    find_hull(S1, L, R, 1,           result, start_time)
    find_hull(S2, R, L, len(result), result, start_time)
    if config.visual:
        draw(start_time)
        plt.savefig(config.image_path)

    return np.array(result)

def find_hull(Sk, A, B, index, result, start_time):
    '''
    Recursive function for  the Quickhull algorithm
    that takes in the set of points to the right of the
    line between P and Q.  Additionally, takes in the
    index of the next point, the list of results, and
    the start time of the timer.
    Returns an array.
    '''
    if not Sk:
        return []

    next_guess = []

    S1 = []
    S2 = []
    C = np.array([])
    dist_C = 0
    for point in Sk:
        dist_Point = utils.dist(A, B, point)
        if dist_C < dist_Point:
            if config.visual:
                if next_guess:
                    next_guess.pop(0).remove()
                x = y = 0
                if index == len(result):
                    x, y = np.vstack((result[-1], point, result[0])).T
                else:
                    x, y = np.vstack((result[index - 1], point,
                            result[index])).T
                next_guess = config.ax.plot(x, y, c=config.n_color,
                        alpha=config.n_alpha, label=config.n_label)
                draw(start_time)
            C = point
            dist_C = dist_Point

    result.insert(index, C)
    if config.visual:
        next_guess.pop(0).remove()
        config.lines.pop(0).remove()
        x, y = np.vstack((result, result[0])).T
        config.lines = config.ax.plot(x, y, c=config.c_color,
                alpha=config.c_alpha, label=config.c_label)

    AtoC = A - C
    CtoB = C - B
    for point in Sk:
        CtoPoint = C - point
        if np.cross(AtoC, CtoPoint)   > 0:
            S1.append(point)
        elif np.cross(CtoB, CtoPoint) > 0:
            S2.append(point)

    orig_len = len(result)
    find_hull(S1, A, C, index, result, start_time)
    next_index = len(result) - orig_len + index + 1
    find_hull(S2, C, B, next_index, result, start_time)


def monotone_chain(points, start_time):
    points = utils.sort_by_x(points)

    upper = []
    lower = []

    next_guess = []

    # Generates a label for guess lines.
    if config.visual:
        next_guess += config.ax.plot([0,0], [0,0], c=config.n_color,
                alpha=config.n_alpha, label=config.n_label)

    for i in range(len(points)):
        while (len(upper) >= 2 and 
               np.cross(upper[len(upper)-1] - upper[len(upper)-2], 
                        points[i] - upper[len(upper)-1]) >= 0):
            upper.pop()
            if config.visual:
                next_guess.pop().remove()
        upper.append(points[i])
        if config.visual and len(upper) > 0:
            x, y = np.vstack((upper[len(upper)-2], points[i])).T
            next_guess += (config.ax.plot(x, y, c=config.n_color, 
                                       alpha=config.n_alpha))
            draw(start_time)

    for i in range(len(points)-1, -1, -1):
        while (len(lower) >= 2 and 
               np.cross(lower[len(lower)-1] - lower[len(lower)-2], 
                        points[i] - lower[len(lower)-1]) >= 0): 
            lower.pop()
            if config.visual:
                next_guess.pop().remove()
        lower.append(points[i])
        if config.visual and len(lower) > 0:
            x, y = np.vstack((lower[len(lower)-2], points[i])).T
            next_guess += (config.ax.plot(x, y, c=config.n_color, 
                                       alpha=config.n_alpha))
            draw(start_time)
    # pprint(upper + lower)
    upper.pop()
    lower.pop()
    if config.visual:
        while next_guess:
            next_guess.pop().remove()
        x, y = np.array(upper + lower + [upper[0]]).T
        config.lines = config.ax.plot(x, y, c=config.c_color,
                alpha=config.c_alpha, label=config.c_label)
        draw(start_time)
        plt.savefig(config.image_path)
    return np.array(upper + lower)

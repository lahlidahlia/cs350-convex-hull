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
    Returns the convex hull as a list.
    The results of this algorithm are out-of-order,
    unlike the other algorithms that have their results in-order.
    '''
    result = []
    convex_points = []
    c_x = []
    c_y = []
    for i in points:
        for j in points:
            if (i == j).all():
                continue
            side = 0
            update = False
            for k in points:
                if (i == k).all() or (j == k).all():
                    continue
                ItoJ = np.subtract(j, i)
                ItoK = np.subtract(i, k)
                newSide = np.cross(ItoJ, ItoK)
                if newSide != 0:
                    if side == 0:
                        side = newSide
                    elif (side < 0 and newSide > 0) or \
                         (side > 0 and newSide < 0):
                        side = False
                        break
                    else:
                        pass
            if side:
                i = list(i)
                j = list(j)
                if i not in result:
                    result.append(i)
                    if config.visual:
                        update = True
                        c_x.append(i[0])
                        c_y.append(i[1])
                if j not in result:
                    result.append(j)
                    if config.visual:
                        update = True
                        c_x.append(j[0])
                        c_y.append(j[1])
                if config.visual and update:
                    if convex_points:
                        convex_points.remove()
                    convex_points = config.ax.scatter(c_x, c_y,
                            s=config.p_area, c=config.c_color,
                            alpha=config.c_alpha, label=config.c_label)
                    draw(start_time)

    if config.visual:
        plt.savefig(config.image_path)
        convex_points.remove()
    return result

def gift_wrap(points, start_time):
    '''
    Gift Wrapping algorithm that takes in the array of
    points and start time of the timer.
    Returns the convex hull as a list.
    '''
    if points.size == 0:
        return []

    result = []
    pointOnHull = utils.left_most_point(points)

    next_guess = []
    c_x = [pointOnHull[0]]
    c_y = [pointOnHull[1]]

    N = len(points)
    endPoint = []
    i = 0
    while True:
        result.append(pointOnHull)
        endPoint = list(points[0])
        oldLine = np.subtract(endPoint,  result[i])

        if config.visual:
            x, y = np.vstack((endPoint,  result[i])).T
            if next_guess:
                next_guess.pop(0).remove()
            next_guess = config.ax.plot(x, y, c=config.n_color,
                    alpha=config.n_alpha, label=config.n_label)
            draw(start_time)
        for j in range(1, N):
            newLine = np.subtract(points[j], result[i])
           
            if endPoint == pointOnHull or np.cross(newLine, oldLine) < 0:
                endPoint = list(points[j])
                oldLine = np.subtract(endPoint,  result[i])
                if config.visual:
                    x, y = np.vstack((endPoint,  result[i])).T
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

        i += 1
        pointOnHull = endPoint

        if endPoint == list(result[0]):
            break
    
    if config.visual:
        plt.savefig(config.image_path)
        next_guess.pop(0).remove()
        draw(start_time)
    return result

def quickhull(points, start_time):
    '''
    Quickhll algorithm that takes in the array of
    points, and the start time of the timer.
    Returns the convex hull as a list.
    '''
    if points.size == 0:
        return []

    A, B = utils.lr_most_point(points)
    result = []
    result.append(A)
    result.append(B)

    if config.visual:
        x, y = np.vstack((A, B)).T
        config.lines = config.ax.plot(x, y, c=config.c_color,
                alpha=config.c_alpha, label=config.c_label)
    S1 = []
    S2 = []
    N = len(points)
    oldLine = np.subtract(result[0], result[1])
    for i in range(N):
        newLine = np.subtract(result[0], points[i])
        if np.cross(oldLine, newLine) > 0:
            S1.append(list(points[i]))
        elif list(points[i]) != result[0] and list(points[i]) != result[1]:
            S2.append(list(points[i]))

    find_hull(S1, result[0],  result[1], 1,           result, start_time)
    find_hull(S2, result[-1], result[0], len(result), result, start_time)
    if config.visual:
        plt.savefig(config.image_path)
        draw(start_time)

    return result

def find_hull(Sk, P, Q, index, result, start_time):
    '''
    Recursive function for  the Quickhull algorithm
    that takes in the set of points to the right of the
    line between P and Q.  Additionally, takes in the
    index of the next point, the list of results, and
    the start time of the timer.
    Returns a list.
    '''
    if not Sk:
        return []

    next_guess = []

    S1 = []
    S2 = []
    C = []
    dist_C = 0
    for point in Sk:
        dist_Point = utils.dist(P, Q, point)
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

    PtoC = np.subtract(P, C)
    CtoQ = np.subtract(C, Q)
    for point in Sk:
        CtoPoint = np.subtract(C, point)
        if np.cross(PtoC, CtoPoint)   > 0:
            S1.append(point)
        elif np.cross(CtoQ, CtoPoint) > 0:
            S2.append(point)

    orig_len = len(result)
    find_hull(S1, P, C, index, result, start_time)
    next_index = len(result) - orig_len + index + 1
    find_hull(S2, C, Q, next_index, result, start_time)


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
               utils.cross(upper[len(upper)-2], 
                           upper[len(upper)-1], 
                           points[i]) >= 0):
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
               utils.cross(lower[len(lower)-2], 
                           lower[len(lower)-1], 
                           points[i]) >= 0):
            lower.pop()
            if config.visual:
                next_guess.pop().remove()
        lower.append(points[i])
        if config.visual and len(lower) > 0:
            x, y = np.vstack((lower[len(lower)-2], points[i])).T
            next_guess += (confg.ax.plot(x, y, c=config.n_color, 
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
    return np.array(upper + lower).tolist()

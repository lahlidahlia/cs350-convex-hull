from sys import argv
import numpy as np
import matplotlib.pyplot as plt

# `gen_rand_points` takes in `N`, the number of points to be generated.
# An array of random, unique points is returned.
# (Returned array could include three or more collinear points)
def gen_rand_points(N):
    x = np.arange(N)
    y = np.arange(N)
    np.random.shuffle(x)
    np.random.shuffle(y)

    return np.column_stack((x, y))

# N = 10
points = gen_rand_points(10)

# Properties of the points
color = 'r'
area  = 20
alpha = 0.75

if '-v' in argv: # Create visualization
    fig, (axG, axQ) = plt.subplots(1, 2, sharey=True)
    x, y = points.T

    # Gift Wrapping algorithm plot
    axG.scatter(x, y, s=area, c=color, alpha=alpha)
    axG.set_title('Gift Wrapping')
    axG.set_xlabel('X')
    axG.set_ylabel('Y')

    # Quick Hull algorithm plot
    axQ.scatter(x, y, s=area, c=color, alpha=alpha)
    axQ.set_title('Quick Hull')
    axQ.set_xlabel('X')

    plt.show()

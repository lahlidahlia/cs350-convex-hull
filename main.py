import random
import numpy as np
import matplotlib.pyplot as plt

visual = True     # Whether or not to generate visualization
N = 20            # Number of generated points
max_value = N * 2 # The max value of each axis
color = 'r'       # The color of the points
area = np.pi * 8  # The area of the points
alpha = 0.75      # Alpha of the points

# Generation of an array of random, unique points
points = random.sample(range(max_value), max_value)
points = np.reshape(points, (-1, 2))

if visual:
    fig, (axG, axQ) = plt.subplots(1, 2, sharey=True)
    x, y = zip(*points)

    axG.scatter(x, y, s=area, c=color, alpha=alpha)
    axG.set_title('Gift Wrapping')
    axG.set_xlabel('X')
    axG.set_ylabel('Y')

    axQ.scatter(x, y, s=area, c=color, alpha=alpha)
    axQ.set_title('Quick Hull')
    axQ.set_xlabel('X')

    plt.show()

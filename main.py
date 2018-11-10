import numpy as np
import matplotlib.pyplot as plt

visual = True    # Whether or not to generate visualization
N = 20           # Number of generated points
max_value = 5    # The max value of each axis
color = 'r'      # The color of the points
area = np.pi * 8 # The area of the points
alpha = 0.75     # Alpha of the points

points = max_value * np.random.rand(N, 2)

if visual:
    fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    x, y = zip(*points)

    ax1.scatter(x, y, s=area, c=color, alpha=alpha)
    ax1.set_title('Gift Wrapping')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')

    ax2.scatter(x, y, s=area, c=color, alpha=alpha)
    ax2.set_title('Quick Hull')
    ax2.set_xlabel('X')

    plt.show()

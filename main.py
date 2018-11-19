import time
import numpy as np
import matplotlib.pyplot as plt
from algorithms import *
from sys import argv
from local import *
from draw import Drawer

if __name__ == '__main__':
    points = np.random.rand(N, 2)
    visual = False
    if '-v' in argv or  '--visual' in argv:
        visual = True
        print("Running with visual mode!")

    start_time = time.time()
    gift_wrap_results = gift_wrap(points)
    print("Gift Wrap results:\n" + str(gift_wrap(points)))
    print("Solved in %.2f seconds" % (time.time() - start_time))

    if visual:
        print("Displaying visuals...")
        drawer = Drawer(points, gift_wrap_results, start_time,
                        "Gift Wrap", "gift_wrap")
        drawer.draw_results()
        plt.show()

    # TODO: Implemented Quick Hull Algorithm
    # if visual:
    #     if lines:
    #         lines.pop(0).remove()
    #     plt.title('Quick Hull')
    #     timer = plt.text(0, 1, "0.0 sec")

    # start_time = time.time()
    # print("Quick Hull results:\n" + str(quick_hull(points)))
    # print("Solved in %.2f seconds" % (time.time() - start_time))

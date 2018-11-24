import time
import numpy as np
import matplotlib.pyplot as plt
import config
from algorithms import *
from draw_algorithms import *
from sys import argv

if __name__ == '__main__':
    points = np.random.rand(config.N, 2)
    gw_results = []
    qh_results = []
    if '-v' in argv or  '--visual' in argv:
        config.visual = True

    if config.visual:
        print("Running with visual mode!")
        init_plot(points)
       
    if config.run_gift_wrap:
        if config.visual:
            reset_plot('Gift Wrap')
        start_time = time.time()
        if config.visual:
            gw_results = draw_gift_wrap(points, start_time)
        else:
            gw_results = gift_wrap(points)
        end_time = time.time() - start_time

        print("Gift Wrap results:\n" + str(gw_results))
        print("Solved in %.2f seconds" % end_time)

    if config.run_quick_hull:
        if config.visual:
            reset_plot('Quick Hull')
        start_time = time.time()
        if config.visual:
            qh_results = draw_quick_hull(points, start_time)
        else:
            qh_results = quick_hull(points)
        end_time = time.time() - start_time

        print("Quick Hull results:\n" + str(qh_results))
        print("Solved in %.2f seconds" % end_time)

    if config.run_gift_wrap and config.run_quick_hull:
        if (np.array(gw_results) == np.array(qh_results)).all():
            print("Results match!")
        else:
            print("Results don't match!")

    if config.visual:
        plt.show()

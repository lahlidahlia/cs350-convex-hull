import time
import numpy as np
import matplotlib.pyplot as plt
import config
from algorithms import *
from sys import argv
from pprint import pprint

if __name__ == '__main__':
    points = np.random.rand(config.N, 2)
    bf_results = []
    gw_results = []
    qh_results = []
    mc_results = []
    if '-v' in argv or '--visual' in argv:
        config.visual = True

    if config.visual:
        print("Running with visual mode\n")
        plt.xlabel('X')
        plt.ylabel('Y')
        config.timer = plt.text(0.9, 1, "")

        init_plot(points)
       
    if config.run_brute_force:
        print("Solving with Brute Force Algorithm")
        if config.visual:
            reset_plot('Brute Force')
        start_time = time.time()
        bf_results = brute_force(points, start_time)
        print(bf_results)
        end_time = time.time() - start_time

        print("Solved in %.2f seconds\n" % end_time)

    if config.run_gift_wrap:
        print("Solving with Gift Wrapping Algorithm")
        if config.visual:
            reset_plot('Gift Wrapping')
        start_time = time.time()
        gw_results = gift_wrap(points, start_time)
        end_time = time.time() - start_time

        print("Solved in %.2f seconds\n" % end_time)

    if config.run_quickhull:
        print("Solving with Quickhull Algorithm")
        if config.visual:
            reset_plot('Quickhull')
        start_time = time.time()
        qh_results = quickhull(points, start_time)
        end_time = time.time() - start_time

        print("Solved in %.2f seconds\n" % end_time)

    if config.run_monotone_chain:
        print("Solving with Monotone Chain Algorithm")
        if config.visual:
            reset_plot('Monotone Chain')
        start_time = time.time()
        mc_results = monotone_chain(points, start_time)
        end_time = time.time() - start_time

        print("Solved in %.2f seconds\n" % end_time)

    # if config.run_brute_force and config.run_gift_wrap:
    #     print("Brute Force and Gift Wrapping comparision:")
    #     if (np.array(bf_results) == np.array(gw_results)).all():
    #         print("\tResults match!")
    #     else:
    #         print("\tResults don't match!")

    # if config.run_brute_force and config.run_quickhull:
    #     print("Brute Force and Quickhull comparision:")
    #     if (np.array(bf_results) == np.array(qh_results)).all():
    #         print("\tResults match!")
    #     else:
    #         print("\tResults don't match!")

    if config.run_gift_wrap and config.run_monotone_chain:
        print("Gift Wrapping and Monotone Chain comparision:")
        if gw_results == mc_results:
            print("\tResults match!")
        else:
            print("\tResults don't match!")
            pprint(gw_results)
            print("------------")
            pprint(mc_results)

    if config.visual:
        plt.show()

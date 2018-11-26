import time
import config
import numpy as np
import matplotlib.pyplot as plt
from sys import argv
from pprint import pprint
from algorithms import *
import datagen as dg

def run_algorithm(algorithm, points):
    algorithms = {
        'Brute Force':    brute_force,
        'Gift Wrapping':  gift_wrap,
        'Quickhull':      quickhull,
        'Monotone Chain': monotone_chain
    }
    function = algorithms.get(algorithm)

    print("Solving with " + algorithm + " Algorithm")
    if config.visual:
        reset_plot(algorithm)
    start_time = time.time()
    results = function(points, start_time)
    end_time = time.time() - start_time
    pprint(results)
    print("Solved in %.2f seconds\n" % end_time)

    with open('results.csv', 'a') as results_file:
        results_file.write("%s,%s,%s\n" %
                (config.dataset, algorithm, str(end_time)))

    return end_time

if __name__ == '__main__':
    # The input dataset
    #points = dg.gen_random_data(10)
    #points = dg.gen_us_cities_data()
    #points = dg.gen_circle(1000)
    #points = dg.gen_triangle(1000)
    points = dg.gen_dense_center(10000)


    # The end times for each algorithm
    bf_time = 0
    gw_time = 0
    qh_time = 0
    mc_time = 0

    if '-v' in argv or '--visual' in argv:
        print("Running with visual mode\n")
        plt.xlabel('X')
        plt.ylabel('Y')
        config.visual = True
        config.timer = plt.text(0.9, 1, "")
        init_plot(points)

    if config.run_brute_force:
        bf_time = run_algorithm('Brute Force', points)

    if config.run_gift_wrap:
        gw_time = run_algorithm('Gift Wrapping', points)

    if config.run_quickhull:
        qh_time = run_algorithm('Quickhull', points)

    if config.run_monotone_chain:
        mc_time = run_algorithm('Monotone Chain', points)

    if config.visual:
        plt.show()

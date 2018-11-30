#!/usr/bin/python3

import time
import config
import random
import statistics
import datagen as dg
import matplotlib.pyplot as plt
from sys import argv
from pprint import pprint
from scipy.spatial import ConvexHull

def run_dataset(dataset, function, sizes):
    '''
    Runs the given dataset on the list of input sizes and the
    corresponding algorithms to run on those.
    '''
    if not config.visual:
        with open(config.timings_file + '.csv', 'a') as results_file:
            results_file.write("%s" % dataset)

    plot = None # Scatter plot
    for size, algos in sizes:
        print("Running {} with {} points".format(dataset, size))
        if config.visual:
            points = function(size)
            # TODO: config.p_area = size somethin'..
            x, y = points.T
            plot = config.ax.scatter(x, y, s=config.p_area,
                    c=config.p_color, alpha=config.p_alpha)
            run_algorithms(dataset, algos, size, points)
            plot.remove()
        else:
            with open(config.timings_file + '.csv', 'a') as results_file:
                results_file.write(",%u," % size)
            times = {a: [] for a in algos}
            for i in range(25): # How many times to run each dataset
                print(str(i+1) + "/25")
                points = function(size)
                timings = run_algorithms(dataset, algos, size, points)
                for name, time in timings.items():
                    times[name].append(time)

            first = True
            print('\nNumber of points: %u' % size)
            for algo, l_time in times.items():
                l_time = l_time[5:] # Removes first 5 timings
                l_time.sort()
                l_time = l_time[6:15] # Grabs median 10 timings

                name, fun = config.algorithms.get(algo)
                print('\nAlgo:\t'  + name)
                print('Mean:\t',   statistics.mean(l_time))
                if not first:
                    with open('results.csv', 'a') as results_file:
                        results_file.write(",,")
                else:
                    first = False
                with open('results.csv', 'a') as results_file:
                    results_file.write("%s,%s\n"
                            % (name,statistics.mean(l_time)))

def run_algorithms(dataset, algos, input_size, points):
    '''
    Runs the given algorithm on the provided input points. Returns a
    dictionary for each algorithm and its end time.
    '''
    times = {a: -1 for a in algos}
    while algos:
        algo = random.choice(algos)
        algos = algos.replace(algo, "")
        algo_name, function = config.algorithms.get(algo)
        config.image_path = 'images/%s-%s-%s.png' \
                % (dataset, algo, str(input_size))

        if config.visual:
            if config.lines:
                config.lines.pop(0).remove()
            config.timer.set_text("0.00 sec")
            config.ax.set_title(
                    "Dataset: %s\nAlgorithm: %s\nData Size: %u" %
                    (dataset, algo_name, input_size))
        start_time = time.time()
        results = function(points, start_time)
        end_time = time.time() - start_time
        times[algo] = end_time * 1000 # Sec to mSec

        # Compare the results to SciPy's
        scipy_results = points[ConvexHull(points).vertices]
        assert all(i in results for i in scipy_results)

    return times

if __name__ == '__main__':
    # Each dataset has a list of sizes with
    # corresponding algorithms to run on each size.
    us_cities_sizes       = []
    major_us_cities_sizes = []
    random_data_sizes     = []
    dense_center_sizes    = []
    circle_sizes          = []

    if '-v' in argv or '--visual' in argv:
        print("Running with visual mode\n")
        # Initialize the visualization
        fig = plt.figure(1)
        config.ax = fig.add_subplot(111)
        config.ax.set_xlabel('X')
        config.ax.set_ylabel('Y')
        config.visual = True
        config.timer = config.ax.text(0.9, 0.95, "",
                ha='center', va='center',
                transform = config.ax.transAxes)

        us_cities_sizes = [
            [35666, 'Q']
        ]
        major_us_cities_sizes = [
            [998, 'GQ']
        ]
        random_data_sizes = [
            [10,      'BGQM'],
            [200,     'BGQM'],
            [500,     'GQ'],
            [998,     'GQ'],
            [10000,   'Q'],
            [35666,   'Q'],
            [100000,  'Q']
        ]
        dense_center_sizes = [
            [100,     'BGQM'],
            [200,     'BGQM'],
            [500,     'BGQ'],
            [998,     'GQ'],
            [10000,   'GQ'],
            [35666,   'GQ'],
            [100000,  'GQ']
        ]
        circle_sizes = [
            [100,     'BQM'],
            [200,     'M']
        ]

    else:
        print("Running with benchmarking mode\n")
        # Write the first row of the CSV file with titles
        with open(config.timings_file + '.csv', 'w') as results_file:
            results_file.write(
                    'Dataset,Input Size,Algorithm,Mean Timing (ms)\n')

        us_cities_sizes = [
            [35666, 'GQM']
        ]
        major_us_cities_sizes = [
            [998, 'GQM']
        ]
        random_data_sizes = [
            [10,      'BGQM'],
            [200,     'BGQM'],
            [500,     'BGQM'],
            [998,     'GQM'],
            [10000,   'GQM'],
            [35666,   'GQM'],
            [100000,  'GQM']
        ]
        dense_center_sizes = [
            [100,     'BGQM'],
            [200,     'BGQM'],
            [500,     'BGQM'],
            [998,     'GQM'],
            [10000,   'GQM'],
            [35666,   'GQM'],
            [100000,  'GQM']
        ]
        circle_sizes = [
            [100,     'BGQM'],
            [200,     'BGQM'],
            [500,     'BGQM'],
            [998,     'GQM'],
            [10000,   'GQM'],
            [35666,   'GQM'],
            [100000,  'GQM']
        ]

    # Run the following datasets:
    run_dataset('US Cities',       dg.gen_us_cities_data,       us_cities_sizes)
    run_dataset('Major US Cities', dg.gen_major_us_cities_data, major_us_cities_sizes)
    if config.visual:
        config.ax.set_xlim([-0.05, 1.05])
        config.ax.set_ylim([-0.05, 1.15])
    run_dataset('Random',          dg.gen_random_data,          random_data_sizes)
    run_dataset('Dense Center',    dg.gen_dense_center,         dense_center_sizes)
    if config.visual:
        config.ax.set_xlim([-1.05, 1.05])
        config.ax.set_ylim([-1.05, 1.15])
    run_dataset('Circle',          dg.gen_circle,               circle_sizes)

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
        if config.visual:
            points = function(size)
            # config.p_area = size somethin'..
            x, y = points.T
            plot = config.ax.scatter(x, y, s=config.p_area,
                    c=config.p_color, alpha=config.p_alpha)
            run_algorithms(dataset, algos, size, points)
            plot.remove()
        else:
            with open(config.timings_file + '.csv', 'a') as results_file:
                results_file.write(",%u," % size)
            times = {a: [] for a in algos}
            for i in range(10): # How many times to run each dataset
                points = function(size)
                timings = run_algorithms(dataset, algos, size, points)
                for name, time in timings.items():
                    times[name].append(time)

            for algo, l_time in times.items():
                name, fun = config.algorithms.get(algo)
                print('ALGO:\t'    + name)
                print('MEDIAN:\t', statistics.median(l_time))
                print('MEAN:\t',   statistics.mean(l_time))
                print('STDEV:\t',  statistics.stdev(l_time))
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
        config.image_path = 'frames/%s_%s_%s.png' \
                % (dataset, algo_name, str(input_size))

        print("Solving with " + algo_name + " Algorithm")
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

        pprint(results)
        print("Solved in %.2f seconds\n" % end_time)

        # Compare the results to SciPy's
        scipy_results = points[ConvexHull(points).vertices].tolist()
        assert all(i in results for i in scipy_results)

    return times

if __name__ == '__main__':
    if '-v' in argv or '--visual' in argv:
        # Initialize the visualization
        print("Running with visual mode\n")
        fig = plt.figure()
        config.ax = fig.add_subplot(111)
        config.ax.set_xlabel('X')
        config.ax.set_ylabel('Y')
        config.visual = True
        config.timer = config.ax.text(0.9, 0.95, "",
                ha='center', va='center',
                transform = config.ax.transAxes)
    else:
        # Write the first row of the CSV file with titles
        with open(config.timings_file + '.csv', 'w') as results_file:
            results_file.write(
                    'Dataset,Input Size,Algorithm,Mean Timing (ms)\n')

    # Run the following datasets:
    # Each dataset has a list of sizes with
    # corresponding algorithms to run on each size.
    #run_dataset('US Cities', dg.gen_us_cities_data, [
    #    [35666, 'Q']
    #])
    if config.visual:
        config.ax.set_xlim([-0.1, 1.1])
        config.ax.set_ylim([-0.1, 1.1])
    run_dataset('Random', dg.gen_random_data, [
        [10,    'BGQ'],
        #[100,   'QM'],
        #[1000,  'M'],
        #[10000, 'Q']
    ])
    #run_dataset('Dense Center', dg.gen_dense_center, [
    #    [10,  'G'],
    #    [100, 'G']
    #])
    #run_dataset('Triangle', dg.gen_triangle, [
    #    [10,  'BGQ'],
    #    [100, 'Q']
    #])
    #if config.visual:
    #    config.ax.set_xlim([-1.1, 1.1])
    #    config.ax.set_ylim([-1.1, 1.1])
    #run_dataset('Circle', dg.gen_circle, [
    #    [10,  'GQ'],
    #    [100, 'G']
    #])
    if config.visual:
        plt.show()

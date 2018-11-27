import time
import config
import datagen as dg
import matplotlib.pyplot as plt
from sys import argv
from pprint import pprint

def run_dataset(dataset, function, sizes):
    with open(config.timings_file + '.csv', 'a') as results_file:
        results_file.write("%s" % dataset)

    plot = None # Scatter plot
    for size, algos in sizes:
        points = function(size)
        if config.visual:
            # config.p_area = size somethin'..
            x, y = points.T
            plot = config.ax.scatter(x, y, s=config.p_area, c=config.p_color,
                    alpha=config.p_alpha)
        run_algorithms(dataset, algos, size, points)
        if config.visual:
            #plot.remove()
            pass

def run_algorithms(dataset_name, algos, input_size, points):
    with open(config.timings_file + '.csv', 'a') as results_file:
        results_file.write(",%u," % input_size)

    first = True
    for algo in algos:
        algo_name, function = config.algorithms.get(algo)
        config.image_path = 'frames/%s_%s_%s.png' \
                % (dataset_name, algo_name, str(input_size))

        print("Solving with " + algo_name + " Algorithm")
        if config.visual:
            if config.lines:
                config.lines.pop(0).remove()
            config.timer.set_text("0.00 sec")
            config.ax.set_title("Dataset: %s\nAlgorithm: %s\nData Size:%u" %
                    (dataset_name, algo_name, input_size))
        start_time = time.time()
        results = function(points, start_time)
        end_time = time.time() - start_time
        pprint(results)
        print("Solved in %.2f seconds\n" % end_time)

        output_size = len(results)
        if not first:
            with open(config.timings_file + '.csv', 'a') as results_file:
                results_file.write(",,")
        else:
            first = False

        with open('results.csv', 'a') as results_file:
            results_file.write("%u,%s,%f\n"
                    % (output_size, algo_name, end_time*1000))

if __name__ == '__main__':
    if '-v' in argv or '--visual' in argv:
        # Initialize the visualization
        print("Running with visual mode\n")
        fig = plt.figure()
        config.ax = fig.add_subplot(111)
        config.ax.set_xlabel('X')
        config.ax.set_ylabel('Y')
        config.visual = True
        config.timer = config.ax.text(0.9, 0.95, "", ha='center', va='center',
                transform = config.ax.transAxes)
   
    # Write the first row of the CSV file with titles
    with open(config.timings_file + '.csv', 'w') as results_file:
        results_file.write('Dataset,Input Size,Output Size,Algorithm,'
        + 'Timing (ms),Worst case number of operations,Operations/ms\n')

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
        #[10,    'BGQ'],
        [100,   'M'],
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

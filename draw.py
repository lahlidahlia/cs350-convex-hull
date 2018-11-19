import matplotlib.pyplot as plt
import numpy as np
from local import *
import time

class Drawer():
    def __init__(self, data_points, results, start_time, title, file_name):
        """
        data_points - All sample data points.
        results - 2D array results of the convex hull algorithm.
        start_time - 
        title - Title of the chart.
        file_name - Name of the file to save frames to.
        """
        self.data_points = data_points
        self.results = results
        self.start_time = start_time
        self.file_name = file_name

        self.timer_text = plt.text(0, 1, "0.0 sec")

        x, y = self.data_points.T
        plt.scatter(x, y, s=p_area, c=p_color, alpha=p_alpha)
        plt.xlabel('X')
        plt.ylabel('Y')

        plt.title(title)

    def draw_results(self):
        """
        Perform the overall frame by frame drawing of the hull algorithm.
        """
        temp_array = []  # Temp array to iterate through draw calls.
        for i in range(len(self.results)):
            temp_array.append(self.results[i])
            self.draw_lines(np.array(temp_array), 
                             "{}_{}".format(self.file_name, str(i)))
        # Connect the last data to the first data.
        self.draw_lines(np.vstack((self.results, self.results[0])), 
                        "{}_{}".format(self.file_name, str(i+1)))

    def draw_lines(self, points, file_name):
        """
        Plots connected lines based on the provided points.
        Displays a timer based on the provided start time.
        Saves a `.png` file of the current frame
        """
        # TODO: separate the actual drawing with saving the file.
        x, y = points.T
        plt.plot(x, y, c=l_color, alpha=l_alpha)
        self.timer_text.set_text("%.2f sec" % (time.time() - self.start_time))
        plt.savefig('frames/' + file_name + '.png')
        plt.pause(visual_delay)

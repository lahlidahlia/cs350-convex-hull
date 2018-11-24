import matplotlib.pyplot as plt
import numpy as np
import config
import time

class _Drawer():
    """
    Singleton. Don't create more than one of this class.
    """
    def __init__(self):
        self.plots = []  # List of plots.
        self.number_of_plots = 0

    def add_plot(self, data_points, title):
        # Add a new plot to the collection and return the plot index.
        new_plot = _Plot(data_points, title)
        self.plots.append(new_plot)
        self.number_of_plots += 1
        return self.number_of_plots - 1

    def add_line(self, p1, p2, time, plot_index):
        self.plots[plot_index].add_line(p1, p2, time)
        

    def draw_all(self):
        """
        Perform the overall frame by frame drawing of the hull algorithm.
        """
        #temp_array = []  # Temp array to iterate through draw calls.
        #for i in range(len(self.results)):
        #    temp_array.append(self.results[i])
        #    self.draw_lines(np.array(temp_array), 
        #                     "{}_{}".format(self.file_name, str(i)))
        ## Connect the last data to the first data.
        #self.draw_lines(np.vstack((self.results, self.results[0])), 
        #                "{}_{}".format(self.file_name, str(i+1)))

        amount = self.number_of_plots
        figure, axes = plt.subplots(amount, sharex='col', sharey='row')
        print(axes)
        for plot_index in range(amount):
            print("Got to " + str(plot_index))
            # Shortener
            plot = self.plots[plot_index]
            axis = axes[plot_index]

            axis.set_title(plot.title)
            data_x, data_y = plot.data_points.T
            axis.scatter(data_x, data_y, s=config.p_area, 
                         c=config.p_color, alpha=config.p_alpha)

            for line in plot.lines:
                # line - [(x1, y1), (x2, y2), time]
                p1, p2, t = line
                self._draw_line(np.vstack((p1, p2)), axis)

        plt.show()


    def _draw_line(self, points, axis):
        """
        Plots connected lines based on the provided points.
        Displays a timer based on the provided start time.
        Saves a `.png` file of the current frame
        """
        # TODO: separate the actual drawing with saving the file.
        x, y = points.T
        axis.plot(x, y, c=config.l_color, alpha=config.l_alpha)
        #self.timer_text.set_text("%.2f sec" % (time.time() - self.start_time))
        #plt.savefig('frames/' + file_name + '.png')
        plt.pause(config.visual_delay)


class _Plot():
    def __init__(self, data_points, title):
        """
        data_points - All sample data points.
        """
        self.data_points = data_points
        self.lines = []  # [[(x1, y1), (x2, y2), time], [...]]
        self.title = title

        #self.timer_text = plt.text(0, 1, "0.0 sec")

        #x, y = self.data_points.T
        #plt.scatter(x, y, s=p_area, c=p_color, alpha=p_alpha)
        #plt.xlabel('X')
        #plt.ylabel('Y')

        #plt.title(title)

    def add_line(self, p1, p2, time):
        self.lines.append([p1, p2, time])


Drawer = _Drawer()

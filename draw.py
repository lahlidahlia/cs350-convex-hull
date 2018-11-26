import time
import config
import matplotlib.pyplot as plt

# The initialization for the scatter plot.
def init_plot(points):
    if points.size == 0:
        return
    x, y = points.T
    plt.scatter(x, y, s=config.p_area, c=config.p_color,
            alpha=config.p_alpha)

# The function to reset the plot.
def reset_plot(title):
    if config.lines:
        config.lines.pop(0).remove()
    config.timer.set_text("0.00 sec")
    plt.title(title)

# Plots connected lines based on the provided points.
# Displays a timer based on the provided start time.
def draw(start_time):
    plt.legend(loc=2)
    config.timer.set_text("%.2f sec" % (time.time() - start_time))
    plt.pause(config.visual_delay)

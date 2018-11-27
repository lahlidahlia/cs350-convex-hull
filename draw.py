import time
import config
import matplotlib.pyplot as plt

def draw(start_time):
    '''
    Plots connected lines based on the provided points.
    Displays a timer based on the provided start time.
    '''
    plt.legend(loc=2)
    config.timer.set_text("%.2f sec" % (time.time() - start_time))
    plt.pause(config.visual_delay)

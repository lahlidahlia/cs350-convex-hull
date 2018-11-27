"""
Contains global variables.
"""
from algorithms import *

# The dictionary of algorithms, each algorithm has a name and a function.
algorithms = {
    'B': ('Brute Force',    brute_force),
    'G': ('Gift Wrapping',  gift_wrap),
    'Q': ('Quickhull',      quickhull),
    'M': ('Monotone Chain', monotone_chain)
}

# The path to the image of the final frame
image_path = ''
# The name of the timings file
timings_file = 'results'
# Delay between frames
visual_delay = 0.0001

# Properties of the points
p_color = 'r'
p_area  = 1
p_alpha = 0.5

# Properties of the convex lines
c_color = 'b'
c_alpha = 0.75
c_label = 'Convex Plot'

# Properties of the next guess lines
n_color = 'm'
n_alpha = 0.75
n_label = 'Next Best'

# Visual components
lines  = []
timer  = None
ax = None
# Whether or not to visualize
visual = False

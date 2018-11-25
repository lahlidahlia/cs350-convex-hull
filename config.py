"""
Contains global variables.
"""

# Whether or not to run each algorithm
run_gift_wrap  = True
run_quick_hull = True

# Number of generated points
N = 50
# Delay between frames
visual_delay = 0.05

# Properties of the points
p_color = 'r'
p_area  = 20
p_alpha = 0.5

# Properties of the convex lines
c_color = 'b'
c_alpha = 0.75
c_label = 'Convex'

# Properties of the next guess lines
n_color = 'm'
n_alpha = 0.75
n_label = 'Next Best'

# Visual components
lines  = []
timer  = None
# Whether or not to visualize
visual = False

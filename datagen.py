import numpy as np
import json

def gen_random_data(amount):
    # Generate data points with random coordinates.
    return np.random.rand(amount, 2)

def gen_us_cities_data():
    ret = None
    #lowest_x = 999
    #highest_x = 0
    #lowest_y = 999
    #highest_y = 0
    with open('us_cities.json') as f:
        ret = json.load(f)

    #for points in ret:
    #    if points[1] < lowest_x:
    #        lowest_x = points[1]
    #    elif points[1] > highest_x:
    #        highest_x = points[1]

    #    if points[0] < lowest_y:
    #        lowest_y = points[0]
    #    elif points[0] > highest_y:
    #        highest_y = points[0]

    #print(lowest_x, highest_x, lowest_y, highest_y)
    return np.array(ret)

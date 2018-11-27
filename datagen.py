import math
import json
import random
import numpy as np

def gen_random_data(amount):
    # Generate data points with random coordinates.
    return np.random.rand(amount, 2)

def gen_us_cities_data(amount):
    data = None
    with open('us_cities.json') as f:
        data = json.load(f)
    return np.array(data)

def gen_circle(amount):
    angle_increment = 360/amount
    radius = 0.75
    
    data = []

    for i in range(amount):
        data.append([math.cos(angle_increment*i)*radius,
                     math.sin(angle_increment*i)*radius])
    return np.array(data)

#def gen_triangle(amount):
#    """
#    Random point on the triangle with vertices pt1, pt2 and pt3.
#    https://stackoverflow.com/questions/47410054/generate-random-locations-within-a-triangular-domain
#    """
#    pt1 = [0.5, 0.1]
#    pt2 = [0.0, 0.0]
#    pt3 = [1.0, 0.0]
#    data = []
#    for _ in range(amount):
#        s, t = sorted([random.random(), random.random()])
#        data.append([s * pt1[0] + (t-s)*pt2[0] + (1-t)*pt3[0],
#                     s * pt1[1] + (t-s)*pt2[1] + (1-t)*pt3[1]])
#    return np.array(data)

def gen_dense_center(amount):
    if amount < 4:
        return None
    
    amount -= 4
    data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    return np.concatenate((data, 0.2 * np.random.rand(amount, 2) + 0.4))

# Pareto distribution checker (constant)

import numpy as np
import random

def generate_pareto_distribution(n_elements, shape):
    return np.random.pareto(shape, n_elements)

def pick_20_percent_magnitude_based(data):
    total_elements = len(data)
    minmin = np.min(data)
    maxmax = np.max(data)
    buckets = [[] for _ in range(5)]
    for d in data:
        buckets[int((d-minmin)/(maxmax-minmin)*4)].append(d)
    
    ind_largest = -1
    largest = -1
    for i, b in enumerate(buckets):
#         print("len(b)", len(b))
        if len(b) > largest:
            ind_largest = i
            largest = len(b)
    return buckets[ind_largest]

def check_pareto(pareto_data):
    pick_size = 0
    data = []
    if len(pareto_data) > 50000:
        pick_size = 50000
        data = np.random.choice(pareto_data, pick_size, replace=True)
    elif len(pareto_data) > 500:
        data = pareto_data
    else:
        print("data is too small")
        return False

    for _ in range(4):
        data_20 = pick_20_percent_magnitude_based(data)
        if len(data_20)/len(data) < .8:
            print("This is not in Pareto")
            return False
        elif len(data_20) < 100:
            print("Too small to detect")
            return False
        data = data_20

    if is_pareto:
        print("This is in Pareto")
        return True


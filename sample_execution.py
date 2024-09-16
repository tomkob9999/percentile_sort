def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore the left half
        elif arr[mid] < target:
            left = mid + 1
        # If target is smaller, ignore the right half
        else:
            right = mid - 1
    
    # If the target is not found
    return -1


import numpy as np
import time
import random

# Function to implement randomized quicksort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return quick_sort(less) + equal + quick_sort(greater)




vector_size = 1000000
vector = np.random.randint(1, vector_size, size=vector_size)
# vector = np.random.random(size=vector_size) * vector_size + 1
# shape_param = 1.1
# vector = np.random.pareto(shape_param, vector_size)


import time
start_time = time.time()
v = np.log(vector)
sorted_dat = p_sort.sort(v)
sorted_dat = np.exp(sorted_dat)
percentile_sort_time = time.time() - start_time
# print("sorted_dat", sorted_dat[:20])
print(f"P Sort Time with log: {percentile_sort_time:.6f} seconds")
print("p_sort.deepest", p_sort.deepest)

start_time = time.time()
sorted_dat = p_sort.sort(vector)
percentile_sort_time = time.time() - start_time
# print("sorted_dat", sorted_dat[:20])
print(f"P Sort Time: {percentile_sort_time:.6f} seconds")
print("p_sort.deepest", p_sort.deepest)




vector_size = 1000000
vector = np.random.randint(1, vector_size, size=vector_size)
# vector = np.random.random(size=vector_size) * vector_size + 1
# shape_param = 1.1
# vector = np.random.pareto(shape_param, vector_size)

import time
start_time = time.time()
sorted_vector, bbb = p_sort.sort(vector, create_btre=True)
percentile_sort_time = time.time() - start_time
# print("sorted_dat", sorted_dat[:20])
print(f"P Sort Time: {percentile_sort_time:.6f} seconds")
print("p_sort.deepest", p_sort.deepest)

siz = int(vector_size/10)


# vec = list(set(sorted_vector))
print("Binary Search")
start_time = time.time()
for i in range(1, siz, 1):
    ret = binary_search(sorted_vector, i)
#     ret = range_search(vec, i, i+100)
#     if ret != -1:
#         print(i, ret)
air_time = time.time() - start_time
print(f"Execution Time: {air_time:.6f} seconds")

print("Percentile Btre Search")
start_time = time.time()
# # ret = bbb.search(101)
# # print(ret)
for i in range(1, siz, 1):
#     print(i)
    ret = bbb.search(i)
#     ret = bbb.search_range(i, i+100)
#     if ret:
#         print(i, ret)
# vals = bbb.search_range(22, 90)
air_time = time.time() - start_time
print(f"Execution Time: {air_time:.6f} seconds")

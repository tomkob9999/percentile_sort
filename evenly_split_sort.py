#
# evenly_split_sort
#
# Description: a divide and conquer sort algorithm that splits by square root percentiles instead of ranks
# This generatates a Van Emde Boas like tree that is accessible with O(loglogn) as by-product
#
# Version: 1.0.1
# Author: Tomio Kobayashi
# Last Update: 2024/9/10

import numpy as np
import math

# # Function to find the minimum and maximum of a vector
# Recursive function to split the array into vectors and merge them
def evenly_split_sort(arr, pmin=-1, pmax=-1, order=None, bb=None):


    # Base case: If the vector contains a single element, return it
    if len(arr) <= 1:
        if bb is not None and len(arr) == 1:
            bb.value1 = arr[0]
        return arr
    
    elif len(arr) == 2:
        if arr[0]>arr[1]:
            arr[0], arr[1] = arr[1], arr[0]

        if bb is not None:
            bb.value1 = arr[0]
            bb.value2 = arr[1]
        return arr


    # Step 1: Find the min and max
#     min_val, max_val = min(arr), max(arr)
    if order is None:
        min_val, max_val = min(arr), max(arr)
        ran = max_val - min_val
    else:
        ran = pmax - pmin
        start = 0
        order = (2,1,1)
        for i, o in enumerate(order):
            ran = np.sqrt(ran)
            start += o*ran
        min_val = pmin + start
        max_val = min_val+ran

    if min_val == max_val:
        if bb is not None:
            bb.value1 = min_val
        return arr
    

    
#     # Step 3: Determine the number of sub-vectors (size sqrt(n))
#     num_buckets = max(2, int(math.sqrt(len(arr))))  # Using square_root(n) as the number of sub-vectors
#     buckets = [[] for _ in range(num_buckets)]


    
    
        
#     Step 3: Determine the number of sub-vectors (size sqrt(n))
#     num_buckets = max(2, int(math.sqrt(len(arr))))  # Using square_root(n) as the number of sub-vectors
    num_buckets = max(2, int(math.sqrt(ran)))  # Using square_root(n) as the number of sub-vectors

    if bb is not None:
#         bb.len = num_buckets
#         bb.len = len(arr)
        bb.len = int(ran)
        bb.min = min_val
        bb.max = max_val

    buckets = [[] for _ in range(num_buckets)]
#     # Step 4: Insert elements into corresponding buckets based on percentile
#     for value in arr:
#         # Calculate the bucket index based on the value's percentile between min and max
#         buckets[min(num_buckets - 1, int((value - min_val) / (max_val - min_val) * num_buckets))].append(value)
        
    # Step 4: Insert elements into corresponding buckets based on percentile
    for value in arr:
        # Calculate the bucket index based on the value's percentile between min and max
        buckets[min(num_buckets - 1, int((value - min_val) / (max_val - min_val) * num_buckets))].append(value)

#     # Step 5: Merge buckets
#     sorted_buckets = []
#     for bucket in buckets:
# #         if bucket:
#         if bb is None :
#             sorted_buckets += percentile_sort(bucket)
#         else:
#             bb.children.append(btre())
#             sorted_buckets += percentile_sort(bucket, bb.children[-1])
#     return sorted_buckets
    
    
    # Step 5: Merge buckets
    sorted_buckets = []
    for i, bucket in enumerate(buckets):
        if bb is None :
            sorted_buckets += evenly_split_sort(bucket, order+(i,) if order is not None else (i,))
        else:
            bb.children.append(btre())
            sorted_buckets += evenly_split_sort(bucket, order+(i,) if order is not None else (i,), bb=bb.children[-1])
    return sorted_buckets
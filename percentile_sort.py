#
# percentile_sort
#
# Description: a divide and conquer sort algorithm that splits by square root percentiles instead of ranks
# This generatates a Van Emde Boas like tree that is accessible with O(loglogn) as by-product
#
# Version: 1.0.10
# Author: Tomio Kobayashi
# Last Update: 2024/9/10

import numpy as np

class btre:
    def __init__(self):
        self.len = -1
        self.min = -np.inf
        self.max = np.inf
        self.children = []
        self.value1 = None
        self.value2 = None

    def search(self, v):
        return self.searchme(v, self)
    
    def searchme(self, v, bb):
        if bb.value1 is not None:
            if v == bb.value1 or v == bb.value2:
                return True
            else:
                return False
        if bb.len == -1:
            return False
        num_buckets = max(2, int(math.sqrt(bb.len))) 
        ind = min(num_buckets - 1, int((v - bb.min) / (bb.max - bb.min) * num_buckets))
        if  ind < 0 or ind > len(bb.children)-1:
            return False
        else:
            return self.searchme(v, bb.children[ind])
        
# Rannge search is too slow because it walks 
#     def search_from(self, s):
#         vals = []
#         self.searchme_from(self, s, vals)
#         return vals
        
#     def searchme_from(self, bb, s, vals):
#         if bb.len == -1:
#             return False
#         if bb.value1 is not None:
#             if bb.value1 >= s:
#                 vals.append(bb.value1)
#                 if bb.value2 is not None and bb.value2 >= s:
#                     vals.append(bb.value2)
#                 return
#         else:
#             if s > bb.max:
#                 return
#             else:
#                 for b in bb.children:
#                     self.searchme_from(b, s, vals)

#     def search_to(self, s):
#         vals = []
#         self.searchme_to(self, s, vals)
#         return vals
    
#     def searchme_to(self, bb, s, vals):
#         if bb.len == -1:
#             return False
#         if bb.value1 is not None:
#             if bb.value1 <= s:
#                 vals.append(bb.value1)
#                 if bb.value2 is not None and bb.value2 <= s:
#                     vals.append(bb.value2)
#                 return
#         else:
#             if s < bb.min:
#                 return
#             else:
#                 for b in bb.children:
#                     self.searchme_to(b, s, vals)
    
#     def search_range(self, s, f):
#         vals = []
#         self.searchme_range(self, s, f, vals)
#         return vals
        
#     def searchme_range(self, bb, s, f, vals):
#         if bb.len == -1:
#             return False
#         if bb.value1 is not None:
#             if bb.value1 >= s and bb.value1 <= f:
#                 vals.append(bb.value1)
#                 if bb.value2 is not None and bb.value2 >= s and bb.value2 <= f:
#                     vals.append(bb.value2)
#                 return
#         else:
#             if s > bb.max or f < bb.min:
#                 return
#             else:
#                 for b in bb.children:
#                     self.searchme_range(b, s, f, vals)
                    
import numpy as np
import math

# # Function to find the minimum and maximum of a vector
# Recursive function to split the array into vectors and merge them
def percentile_sort(arr, bb=None):
    
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
    min_val, max_val = min(arr), max(arr)
    if min_val == max_val:
        bb.value1 = min_val
        return arr

    if bb is not None:
        bb.len = len(arr)
        bb.min = min_val
        bb.max = max_val
    
    # Step 3: Determine the number of sub-vectors (size sqrt(n))
    num_buckets = max(2, int(math.sqrt(len(arr))))  # Using square_root(n) as the number of sub-vectors
    buckets = [[] for _ in range(num_buckets)]

    # Step 4: Insert elements into corresponding buckets based on percentile
    for value in arr:
        # Calculate the bucket index based on the value's percentile between min and max
        buckets[min(num_buckets - 1, int((value - min_val) / (max_val - min_val) * num_buckets))].append(value)
        
    # Step 5: Merge buckets
    sorted_buckets = []
    for bucket in buckets:
#         if bucket:
        if bb is None :
            sorted_buckets += percentile_sort(bucket)
        else:
            bb.children.append(btre())
            sorted_buckets += percentile_sort(bucket, bb.children[-1])
    return sorted_buckets

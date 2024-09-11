#
# percentile_sort
#
# Description: a divide and conquer sort algorithm that splits by square root percentiles instead of ranks
# This generatates a Van Emde Boas like tree that is accessible with O(loglogn) as by-product
#
# Version: 1.1.1
# Author: Tomio Kobayashi
# Last Update: 2024/9/11

import numpy as np

class btre:
    def __init__(self):
        self.len = -1
        self.min = -np.inf
        self.max = np.inf
        self.children = []
        self.value1 = None
        self.value2 = None
        
        self.left = None
        self.right = None
        self.top = None
        self.last = None

    def search(self, v, return_node=False):
        return self.searchme(v, self, return_node)
    
    def searchme(self, v, bb, return_node=False):
        if bb.value1 is not None:
            if v == bb.value1 or v == bb.value2:
                return True if not return_node else bb
            else:
                return False if not return_node else None
        if bb.len == -1:
            return False
        num_buckets = max(2, int(math.sqrt(bb.len))) 
        ind = min(num_buckets - 1, int((v - bb.min) / (bb.max - bb.min) * num_buckets))
        if  ind < 0 or ind > len(bb.children)-1:
            return False if not return_node else None
        else:
            return self.searchme(v, bb.children[ind], return_node)
        
    def link(self, sorted_vector):
        prev = None
        for i, v in enumerate(sorted_vector):
            if i == 0:
                prev = self.search(sorted_vector[i], return_node=True)
                self.top = prev
            else:
                nex_val = sorted_vector[i]
                if sorted_vector[i-1] == sorted_vector[i]:
                    continue
                nex = bbb.search(sorted_vector[i], return_node=True)
                if nex == prev:
                    continue
                prev.right = nex
                nex.left = prev
                self.last = nex
                prev = nex

    def search_from(self, s):
        vals = []
        pos = self.last
        while pos:
            if pos.value1 and pos.value1 >= s:
                vals.append(pos.value1)
            else:
                break
            if pos.value2 and pos.value2 >= s:
                vals.append(pos.value2)
            pos = pos.left
        vals.reverse()
        return vals


    def search_to(self, s):
        vals = []
        pos = self.top
        while pos:
            if pos.value1 and pos.value1 <= s:
                vals.append(pos.value1)
            else:
                break
            if pos.value2 and pos.value2 <= s:
                vals.append(pos.value2)
            pos = pos.right
        return vals
    
    def search_range(self, s, f):
        vals = []
        pos = self.searchme_range(self, s, f, vals)
        pos = pos.right
        while pos:
            if pos.value1 and pos.value1 <= f:
                vals.append(pos.value1)
            else:
                break
            if pos.value2 and pos.value2 <= f:
                vals.append(pos.value2)
            pos = pos.right
        return vals


    def searchme_range(self, bb, s, f, vals):
        if bb.value1 is not None:
            if bb.value1 >= s and bb.value1 <= f:
                vals.append(bb.value1)
                if bb.value2 is not None and bb.value2 >= s and bb.value2 <= f:
                    vals.append(bb.value2)
                return bb
        else:
            if s > bb.max or f < bb.min:
                return None
            else:
                for b in bb.children:
                    pos = self.searchme_range(b, s, f, vals)
                    if vals:
                        return pos
                    
                    
import numpy as np
import math

# # Function to find the minimum and maximum of a vector
# Recursive function to split the array into vectors and merge them
def percentile_sort(arr, bb=None, link=False):
    
    if len(arr) <= 1:
        if bb is not None and len(arr) == 1:
            bb.value1 = arr[0]
        return arr
    elif len(arr) == 2:
        if arr[0]>arr[1]:
            arr[0], arr[1] = arr[1], arr[0]

        if bb is not None:
            if arr[0] == arr[1]:
                bb.value1 = arr[0]
            else:
                bb.value1 = arr[0]
                bb.value2 = arr[1]
        return arr

    # Find the min and max
    min_val, max_val = min(arr), max(arr)
    if min_val == max_val:
        bb.value1 = min_val
        return arr

    if bb is not None:
        bb.len = len(arr)
        bb.min = min_val
        bb.max = max_val
    
    num_buckets = max(2, int(math.sqrt(len(arr))))  # Using square_root(n) as the number of sub-vectors
    buckets = [[] for _ in range(num_buckets)]

    # Insert elements into corresponding buckets based on percentile
    for value in arr:
        # Calculate the bucket index based on the value's percentile between min and max
        buckets[min(num_buckets - 1, int((value - min_val) / (max_val - min_val) * num_buckets))].append(value)
        
    # Merge buckets
    sorted_buckets = []
    for bucket in buckets:
        if bb is None :
            sorted_buckets += percentile_sort(bucket)
        else:
            bb.children.append(btre())
            sorted_buckets += percentile_sort(bucket, bb.children[-1])
            
    if bb is not None and link:
        bb.link(sorted_buckets)
        
    return sorted_buckets

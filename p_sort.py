#
# p_sort
#
# Description: a divide and conquer sort algorithm that splits by square root percentiles instead of ranks
# This optionally generatates a Van Emde Boas like tree that is accessible with O(loglogn) as by-product
#
# Version: 1.3.0
# Author: Tomio Kobayashi
# Last Update: 2024/9/17

import numpy as np
import math

# # Function to find the minimum and maximum of a vector
# Recursive function to split the array into vectors and merge them
class p_sort:
    
    ROOT_POWER = 1.25 # n^(1/1.25) seems faster than n^(1/2)(=square root)
    deepest = 0
    
    class btre:
        def __init__(self):
            self.len = -1
            self.min = -np.inf
            self.max = np.inf
            self.children = []
            
            self.pos1 = -1
            self.pos2 = -1
#             self.sorted_set = None
            self.sorted_set = []

        def search(self, v, return_node=False):
            return self.searchme(v, self, return_node)
        
        def searchme(self, v, bb, return_node=False):
            if bb.len == -1:
                return -1 if not return_node else None
            if bb.len == 0:
                if v == bb.min:
                    return bb.pos1 if not return_node else bb
                elif v == bb.max:
                    return bb.pos2 if not return_node else bb
                else:
                    return -1 if not return_node else None
            
            num_buckets = max(2, int(bb.len**(1/p_sort.ROOT_POWER)))
            ind = min(num_buckets - 1, int((v - bb.min) / (bb.max - bb.min) * num_buckets))
            if  ind < 0 or ind > len(bb.children)-1:
                return -1 if not return_node else None
            else:
                return self.searchme(v, bb.children[ind], return_node)
                    
        def link(self, sorted_vector):
            prev = np.inf
            for i, v in enumerate(sorted_vector):
                if prev != sorted_vector[i]:
                    bb = self.search(sorted_vector[i], return_node=True)
                    if sorted_vector[i] == bb.min:
                        bb.pos1 = len(self.sorted_set)
                    elif sorted_vector[i] == bb.max:
                        bb.pos2 = len(self.sorted_set)
                    prev = sorted_vector[i]
                    self.sorted_set.append(sorted_vector[i])
#             self.sorted_set = sorted_vector
                
#         def link(self, sorted_vector):
#             prev = np.inf
#             for i, v in enumerate(sorted_vector):
#                 if prev != sorted_vector[i]:
#                     bb = self.search(sorted_vector[i], return_node=True)
#                     if sorted_vector[i] == bb.min:
#                         bb.pos1 = i
#                     elif sorted_vector[i] == bb.max:
#                         bb.pos2 = i
#                     prev = sorted_vector[i]
# #                     self.sorted_set.append(sorted_vector[i])
#             self.sorted_set = sorted_vector

        def search_from(self, s):
            suc = self.succ(s)
            if suc == -1:
                return []
            return self.sorted_set[suc:]
        
        def search_to(self, f):
            pre = self.prec(f)
            if pre == -1:
                return []
            return self.sorted_set[:pre+1]
        
        def search_range(self, s, f):
            suc = self.succ(s)
            pre = self.prec(f)
            if pre < suc or suc == -1 or pre == -1:
                return []
            return self.sorted_set[suc:pre+1]
            

        def succ(self, s):
            return self.succme(self, s)
            
        def succme(self, bb, s):
            if bb.len == -1:
                    return -1                
            if bb.len == 0:
                if s <= bb.min:
                    return bb.pos1
                elif s <= bb.max:
                    return bb.pos2
                else:
                    return -1
            else: 
                num_buckets = max(2, int(bb.len**(1/p_sort.ROOT_POWER)))
                ind = min(num_buckets - 1, int((s - bb.min) / (bb.max - bb.min) * num_buckets))
                if ind > len(bb.children)-1:
                    return -1
                for i in range(max(0, ind), len(bb.children), 1):
                    pos = self.succme(bb.children[i], s)
                    if pos > -1:
                        return pos
                return -1

        def prec(self, f):
            return self.precme(self, f)
            
        def precme(self, bb, s):
            if bb.len == -1:
                    return -1                
            if bb.len == 0:
                if s >= bb.max:
                    return bb.pos2
                elif s >= bb.min:
                    return bb.pos1
                else:
                    return -1
            else: 
                num_buckets = max(2, int(bb.len**(1/p_sort.ROOT_POWER)))
                ind = min(num_buckets - 1, int((s - bb.min) / (bb.max - bb.min) * num_buckets))
                if ind < 0:
                    return -1
                for i in range(min(len(bb.children)-1, ind), -1, -1):
                    pos = self.precme(bb.children[i], s)
                    if pos > -1:
                        return pos
                return -1
            
        def update(self, inserts=[], deletes=[]):
            c = self.sorted_set[0:]
            for d in deletes:
                c.remove(d)
            for i in inserts:
                c.append(i)
            return p_sort.sort(c, create_btre=True, link=True)
            
    def sort(arr, create_btre=False, find_depth=True):
        depth = -1
        p_sort.deepest = 0
        if find_depth:
            depth = 0
            
        if create_btre:
            bb = p_sort.btre()
            sorted_vector = p_sort.percentile_sort(arr, bb, depth=depth)
            if bb is not None:
#                 bb.link(list(set(sorted_vector)))
                bb.link(sorted_vector)
#                 bb.link(list(sorted_vector))
#                 ll = []
#                 prev = np.inf
#                 for s in sorted_vector:
#                     if s != prev:
#                         ll.append(s)
#                         prev = s
#                 bb.link(ll)
            return sorted_vector, bb
        else:
            return p_sort.percentile_sort(arr, depth=depth)
        
    def percentile_sort(arr, bb=None, depth=-1):
        if depth > -1:
            depth += 1
            if depth > p_sort.deepest:
                p_sort.deepest = depth
        
        if len(arr) <= 1:
            if bb is not None and len(arr) == 1:
                bb.min = arr[0]
                bb.len = 0
            return arr
        elif len(arr) == 2:
            if arr[0]>arr[1]:
                arr[0], arr[1] = arr[1], arr[0]

            if bb is not None:
                if arr[0] == arr[1]:
                    bb.min = arr[0]
                else:
                    bb.min = arr[0]
                    bb.max = arr[1]
                bb.len = 0
            return arr

        # Find the min and max
        min_val, max_val = min(arr), max(arr)
        if min_val == max_val:
            if bb is not None:
                bb.min = arr[0]
                bb.len = 0
            return arr

        if bb is not None:
            bb.len = len(arr)
            bb.min = min_val
            bb.max = max_val

        num_buckets = max(2, int(len(arr)**(1/p_sort.ROOT_POWER)))
        buckets = [[] for _ in range(num_buckets)]
#         minmin = [[np.inf] for _ in range(num_buckets)]
#         maxmax = [[-np.inf] for _ in range(num_buckets)]

        # Insert elements into corresponding buckets based on percentile
        for value in arr:
            # Calculate the bucket index based on the value's percentile between min and max
            buckets[min(num_buckets - 1, int((value - min_val) / (max_val - min_val) * num_buckets))].append(value)
        # Merge buckets
        sorted_buckets = []
        for bucket in buckets:
            if bb is None :
                sorted_buckets += p_sort.percentile_sort(bucket, depth=depth)
            else:
                bb.children.append(p_sort.btre())
                sorted_buckets += p_sort.percentile_sort(bucket, bb.children[-1], depth=depth)

#         if bb is not None:
#             bb.link(list(set(sorted_buckets)))

        return sorted_buckets
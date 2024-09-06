#
# percentile_sort
#
# Description: Divide and Conquert Sort that uses percentiles instead of ranks to avoid individual comparison and save merge workload unlike quick sort or merge sort
# Version: 1.0.1
# Author: Tomio Kobayashi
# Last Update: 2024/9/6

import numpy as np
import math

# # Function to find the minimum and maximum of a vector

# Recursive function to split the array into vectors and merge them
def percentile_sort(arr):
    # Base case: If the vector contains a single element, return it
    if len(arr) <= 1:
        return arr
    elif len(arr) == 2:
        if arr[0]>arr[1]:
            a = arr[1]
            arr[1] = arr[0]
            arr[0] = a
        return arr
#     else:
#         f = arr[0]
#         if all(a == f for a in arr[1:]):
#             return arr
#     print("arr", arr)

    # Step 1: Find the min and max
#     min_val, max_val = find_min_max(arr)
    min_val, max_val = min(arr), max(arr)

    # Step 2: If all elements are the same, return the array
    if min_val == max_val:
        return arr

    # Step 3: Determine the number of sub-vectors (size log(n))
    n = len(arr)
#     num_buckets = max(1, int(math.log2(n)))  # Using log2(n) as the number of sub-vectors
#     num_buckets = max(2, int(math.log2(n)))  # Using log2(n) as the number of sub-vectors
    num_buckets = max(2, int(math.sqrt(n)))  # Using log2(n) as the number of sub-vectors
    
#     print("math.log2(n)", math.log2(n))
    buckets = [[] for _ in range(num_buckets)]

    # Step 4: Insert elements into corresponding buckets based on percentile
    for value in arr:
        # Calculate the bucket index based on the value's percentile between min and max
#         if max_val == min_val:
#             bucket_index = 0
#         else:
#             bucket_index = min(num_buckets - 1, int((value - min_val) / (max_val - min_val) * num_buckets))
        bucket_index = min(num_buckets - 1, int((value - min_val) / (max_val - min_val) * num_buckets))
        buckets[bucket_index].append(value)

    # Step 5: Recursively sort each bucket
    if sum([1 for b in buckets if len(b) > 0]) == 1:
        return [b for b in buckets if len(b) > 0][0]

    sorted_buckets = []
    for bucket in buckets:
        if bucket:
#             sorted_buckets.append(percentile_sort(bucket))
            sorted_buckets.extend(percentile_sort(bucket))
    return sorted_buckets

#     # Step 6: Merge sorted buckets
#     result = []
#     for bucket in sorted_buckets:
#         result.extend(bucket)
    
#     return result

# Example usage
n = 16  # Size of the vector
vector = np.random.randint(1, 101, size=n)  # Generate a random vector of integers between 1 and 100

print("Original vector:", vector)

# Perform the recursive sort
sorted_vector = percentile_sort(vector.tolist())

# Display the sorted vector
print("Sorted vector:", sorted_vector)
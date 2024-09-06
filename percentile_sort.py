#
# percentile_sort
#
# Description: a divide and conquer sort algorithm that splits by square root percentiles instead of ranks
# Version: 1.0.4
# Author: Tomio Kobayashi
# Last Update: 2024/9/7

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
            arr[0], arr[1] = arr[1], arr[0]
        return arr

    # Step 1: Find the min and max
    min_val, max_val = min(arr), max(arr)

    # Step 2: If all elements are the same, return the array
    if min_val == max_val:
        return arr

    # Step 3: Determine the number of sub-vectors (size log(n))
    n = len(arr)

    num_buckets = max(2, int(math.sqrt(n)))  # Using square_root(n) as the number of sub-vectors
    
    buckets = [[] for _ in range(num_buckets)]

    # Step 4: Insert elements into corresponding buckets based on percentile
    for value in arr:
        # Calculate the bucket index based on the value's percentile between min and max
        bucket_index = min(num_buckets - 1, int((value - min_val) / (max_val - min_val) * num_buckets))
        buckets[bucket_index].append(value)
        
    # Step 5: Merge buckets
    sorted_buckets = []
    for bucket in buckets:
        if bucket:
            sorted_buckets.extend(percentile_sort(bucket))
    return sorted_buckets

# Example usage
n = 16  # Size of the vector
# vector = np.random.randint(1, 101, size=n)  # Generate a random vector of integers between 1 and 100
vector = np.random.random(size=n) * 100 + 1

print("Original vector:", vector)

# Perform the recursive sort
sorted_vector = percentile_sort(vector.tolist())

# Display the sorted vector
print("Sorted vector:", sorted_vector)

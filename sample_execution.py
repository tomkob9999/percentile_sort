# Example usage
n = 100  # Size of the vector
vector = np.random.randint(1, 101, size=n)  # Generate a random vector of integers between 1 and 100
# # vector = np.random.random(size=n) * n
# n = 100000  # Size of the vector
# vector = np.random.randint(1, n, size=n)  # Generate a random vector of integers between 1 and 100
# n = 100000
# vector = np.random.random(size=n) * n

print("Original vector:", vector[:50])


# # Perform the recursive sort
import time
print("p_sort")
start_time = time.time()
sorted_vector, bbb = p_sort.sort(vector.tolist(), create_btre=True, link=True)
# sorted_vector = p_sort.sort(vector.tolist(), create_btre=False, link=True)
air_time = time.time() - start_time
print(f"Execution Time: {air_time:.6f} seconds")


# print("Sorted vector:")
print("Percentile sorted vector:")
print(sorted_vector[:50])
# print(sorted_vector)
print("len(sorted_vector)", len(sorted_vector))

ret = bbb.search(8)
print("ret", ret)


ret = bbb.search(20)
print("ret", ret)
print("sorted_set", bbb.sorted_set[ret])
ret = bbb.succ(24)
# print("ret", ret)
print("sorted_set", bbb.sorted_set[ret])
ret = bbb.prec(29)
print("ret", ret)
print("sorted_set", bbb.sorted_set[ret])
ret = bbb.search_range(22, 40)
print("ret", ret)
ret = bbb.search_from(22)
print("ret", ret)
ret = bbb.search_to(41)
print("ret", ret)

new, bb2 = bbb.update([101])
print("new", new)

new, bb3 = bb2.update([105])
print("new", new)

new, bb3 = bb3.update([], [101])


#######
# sample test data creation
#

# Create a vector of random integers between 1 and 1000
# vector_size = 20000000
# vector = np.random.randint(1, vector_size, size=vector_size)

# vector_size = 1000000
# vector = np.random.randint(1, vector_size, size=vector_size)

# Test with skewed data
# scale = 10000.0  # The scale parameter (1/λ). Lower values increase the skewness.
# vector = np.random.exponential(scale, n)
# mean = 1000
# std_dev = 1
# vector = np.random.normal(mean, std_dev, n)
# shape, scale = 0.5, 1.0  # Shape controls the skewness; scale adjusts the spread
# vector = np.random.gamma(shape, scale, n)


# Quick sort implementation used in testin

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return quick_sort(less) + equal + quick_sort(greater)



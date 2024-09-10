
# Example usage
# n = 100  # Size of the vector
# vector = np.random.randint(1, 101, size=n)  # Generate a random vector of integers between 1 and 100
# n = 100000  # Size of the vector
# vector = np.random.randint(1, n, size=n)  # Generate a random vector of integers between 1 and 100
n = 500000
vector = np.random.random(size=n) * n

print("Original vector:", vector[:50])

bbb = btre()
# sorted_vector = evenly_split_sort(vector.tolist(), bbb)
# sorted_vector = evenly_split_sort(vector.tolist())
# sorted_vector = percentile_sort(vector.tolist(), bbb)
# sorted_vector = evenly_split_sort(vector.tolist())


# # Perform the recursive sort
import time
print("evenly_split_sort")
start_time = time.time()
# sorted_vector_even = evenly_split_sort(vector.tolist())
bbe = btre()
sorted_vector_even = evenly_split_sort(vector.tolist(), bb=bbe)
air_time = time.time() - start_time
print(f"Execution Time: {air_time:.6f} seconds")

print("percentile_sort")
start_time = time.time()
# sorted_vector = percentile_sort(vector.tolist())
bbb = btre()
sorted_vector = percentile_sort(vector.tolist(), bbb)
air_time = time.time() - start_time
print(f"Execution Time: {air_time:.6f} seconds")

# # Display the sorted vector
print("Even sorted vector:")
print(sorted_vector_even[:50])
# Display the sorted vector
print("Sorted vector:")
print("Percentile sorted vector:")
print(sorted_vector[:50])

# # Perform the recursive sort
# import time
# print("Search")
# start_time = time.time()
# # ret = bbb.search(int(n/2))
# ret = bbb.search(101)
# air_time = time.time() - start_time
# print(ret)
# print(f"Execution Time: {air_time:.6f} seconds")

# start_time = time.time()
# # xx = bbb.search_range(13, 49)
# xx = bbb.search_range(1000, 2000)
# air_time = time.time() - start_time
# print(xx[:10])
# print(f"Execution Time: {air_time:.6f} seconds")

# print(bbb.search_from(13))
# print(bbb.search_to(49))
# print(bbb.search_range(13, 49))

for i in range(1, 50, 1):
    ret = bbb.search(i)
    if ret:
        print("bbb ", i, ret)
for i in range(1, 50, 1):
    ret = bbe.search(i)
    if ret:
        print("bbe ", i, ret)

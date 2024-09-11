# Example usage
n = 100  # Size of the vector
vector = np.random.randint(1, 101, size=n)  # Generate a random vector of integers between 1 and 100
# vector = np.random.random(size=n) * n
# n = 100000  # Size of the vector
# vector = np.random.randint(1, n, size=n)  # Generate a random vector of integers between 1 and 100
# n = 500000
# vector = np.random.random(size=n) * n

print("Original vector:", vector[:50])


# # Perform the recursive sort
import time
print("percentile_sort")
start_time = time.time()
# sorted_vector = p_sort.percentile_sort(vector.tolist())
bbb = p_sort.btre()
sorted_vector = p_sort.percentile_sort(vector.tolist(), bbb, link=True)
# sorted_vector = p_sort.percentile_sort(vector.tolist())
air_time = time.time() - start_time
print(f"Execution Time: {air_time:.6f} seconds")


print("Sorted vector:")
print("Percentile sorted vector:")
print(sorted_vector[:50])
# print(sorted_vector)
print("len(sorted_vector)", len(sorted_vector))



ret = bbb.search(8)
print("ret", ret)

vals = bbb.search_range(8, 20)
print(vals)
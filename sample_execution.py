
# Example usage
# n = 100  # Size of the vector
# vector = np.random.randint(1, 101, size=n)  # Generate a random vector of integers between 1 and 100
# n = 100000  # Size of the vector
# vector = np.random.randint(1, n, size=n)  # Generate a random vector of integers between 1 and 100
n = 500000
vector = np.random.random(size=n) * n

print("Original vector:", vector[:50])

# bbb = btre()
# sorted_vector = percentile_sort(vector.tolist(), bbb)
# sorted_vector = percentile_sort(vector.tolist())


# # Perform the recursive sort

print("percentile_sort")
start_time = time.time()
# sorted_vector = percentile_sort(vector.tolist())
bbb = btre()
sorted_vector = percentile_sort(vector.tolist(), bbb)
air_time = time.time() - start_time
print(f"Execution Time: {air_time:.6f} seconds")

# # Display the sorted vector
# Display the sorted vector
print("Sorted vector:")
print("Percentile sorted vector:")
print(sorted_vector[:50])


for i in range(1, 50, 1):
    ret = bbb.search(i)
    if ret:
        print("bbb ", i, ret)

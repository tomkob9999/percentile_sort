# percentile_sort

This seems faster than other nlogn sorting algorithms.  Seems to outperform more as the data size grows and more duplicate elements exist

The time complexity seems to be: $T(n) = \sqrt{n} \cdot T(\sqrt{n}) + O(n)$.

And which would leads to: $O(n \log \log n)$.

**Sample Test Result** (with vector of size 5,000,000 filled with random integers between 1 and 5,000,000)  
- **Randomized Quick Sort Time**: 46.416540 seconds  
- **Percentile Sort Time**: 19.905263 seconds  
- **Do-Nothing Loop Time**: 0.908326 seconds
- On a side note, while this test data contains a small portion of duplicates, percentile_sort shows tendency to be faster as duplicates increase.

### Pseudocode for `percentile_sort`

```pseudo
percentile_sort(input_array):

  if size(input_array) <= 1 then
     return input_array
  else if size(input_array) <= 2 then
     if input_array[1] < input_array[0] then
        input_array[0], input_array[1] = input_array[1], input_array[0]

  min_value = min(input_array)  -- O(1)
  max_value = max(input_array)  -- O(1)

  if min_value == max_value then
     return input_array

  num_buckets = max(2, square_root(size(input_array)))  -- O(1)

  foreach value in input_array  -- loops n times, time complexity O(n)
     bucket_index = integer((value - min_value)/(max_value - min_value) * num_buckets)  -- O(1)
     buckets[bucket_index].append(value)

  foreach bucket in buckets  -- loop square_root(n) times, time complexity T(square_root(n))
     if bucket is not empty
        sorted_buckets.append(percentile_sort(bucket))  -- recursive call

  return sorted_buckets

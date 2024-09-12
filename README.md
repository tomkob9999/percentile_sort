# percentile_sort

This seems faster than other nlogn sorting algorithms.  Seems to outperform more as the data size grows and more duplicate elements exist

The time complexity seems to be: $T(n) = \sqrt{n} \cdot T(\sqrt{n}) + O(n)$, which would lead to: $O(n \log \log n)$.

**Sample Test Result** (with vector of size 5,000,000 filled with random integers between 1 and 5,000,000)  
- **Randomized Quick Sort Time**: 46.416540 seconds  
- **Percentile Sort Time**: 19.905263 seconds  
- **Do-Nothing Loop Time**: 0.908326 seconds
- On a side note, while this test data contains a small portion of duplicates, percentile_sort shows tendency to be faster as duplicates increase.


Sample Test Statistics with another input data of size 1,000,000.  The time complexity was equivalent of above.

Float type
| Sort Type              | Recursion Depth | Number of calls | Average Input Size |
|------------------------|-----------------|-----------------|--------------------|
| Percentile Sort         | 10               | 1105716          | 5.46              |
| Randomized Quick Sort   | 51              | 1333631          | 18.99             |

Integer Type
| Sort Type              | Recursion Depth | Number of calls | Average Input Size |
|------------------------|-----------------|-----------------|--------------------|
| Percentile Sort         | 4                | 193389          | 20.68              |
| Randomized Quick Sort   | 41               | 199911          | 102.60             |

As by-product,  a static van-Edme-Boas-like tree is generated as output.  The time complexity of matching search is: $T(n) = T(\sqrt{n}) + O(1)$, which leads to: $O(\log \log n)$.  It has also range search and update (it basically regenarates the array and tree, so the time complexity is the same as sorting..

### Pseudocode for `p_sort`

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
     append value to buckets[bucket_index]

  foreach bucket in buckets  -- loop square_root(n) times, time complexity T(square_root(n))
        call percentile_sort(bucket)  -- recursive call
        append return vector to sorted_buckets

  return sorted_buckets
```



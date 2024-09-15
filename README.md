# p_sort

This algorithm seems faster than other nlogn sorting algorithms.  It seems to outperform more as the data size grows and more duplicate elements exist

The time complexity seems to be: $T(n) = \sqrt{n} \cdot T(\sqrt{n}) + O(n)$, which would lead to: $O(n \log \log n)$.

This algorithm divides into $\sqrt{n}$ pieces in $O(n)$ while Merge Sort takes $O(1)$ and Quick Sort takes $O(n)$ to both divide into 2.  This algorithm takes $O(\sqrt{n})$ to merge while Merge Sort takes $O(n)$ and Quick Sort takes $O(1)$.

**Sample Test Result** (with vector of size 5,000,000 filled with random integers between 1 and 5,000,000)  
- **Randomized Quick Sort Time**: 46.416540 seconds  
- **P-Sort Time**: 19.905263 seconds  
- **Do-Nothing Loop Time**: 0.908326 seconds
- On a side note, while this test data contains a small portion of duplicates, percentile_sort shows tendency to be faster as duplicates increase.

NOTE: For very skewed data that is recursively very concentrated like Pareto distribution, the conversion could be slow.  To counter-act this, such distribution can be detected in O(1) time (sampled, pareto_cheker.py) and then it could preprocess the data by logging the input data to linearize the shape and then exponentiate back later, or keep the index during sorting and use it at the end, which is in total O(n), as sampled in percentile_sort_linearize_preprocess_version.py.


Sample Test Statistics with another input data of size 1,000,000.  The time complexity was equivalent of above.

Float type
| Sort Type              | Recursion Depth | Number of calls | Average Input Size |
|------------------------|-----------------|-----------------|--------------------|
| P Sort         | 10               | 1105716          | 5.46              |
| Randomized Quick Sort   | 51              | 1333631          | 18.99             |

Integer Type
| Sort Type              | Recursion Depth | Number of calls | Average Input Size |
|------------------------|-----------------|-----------------|--------------------|
| P Sort         | 4                | 193389          | 20.68              |
| Randomized Quick Sort   | 41               | 199911          | 102.60             |

### Pseudocode for `p_sort`

```pseudo
percentile_sort(input_array):

  if size(input_array) <= 1 then
     return input_array
  else if size(input_array) <= 2 then
     if input_array[1] < input_array[0] then
        input_array[0], input_array[1] = input_array[1], input_array[0]

  min_value = min(input_array)  -- O(1) by calculating in the previous loop for each bucket, but O(n) implementation doesn't change the time complexity.  Same for max and len.
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

As by-product,  a m-ary tree is generated as output.  The time complexity of matching search seems: $T(n) = T(\sqrt{n}) + O(1)$, which would lead to: $O(\log \log n)$.  It has also range search and update (but the current implementation only re-sorts and regenarates the outputs for updates, so the time complexity is the same as sorting.  Updates with $O(\log \log n)$ time (search time with constant) seem possible, but no plan of implementation as of now.


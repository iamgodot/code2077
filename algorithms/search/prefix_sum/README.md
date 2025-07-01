# Prefix Sum

Using prefix sum allows us to quickly find the sum of any subarray.

We usually define prefix_sum[i] as the sum of the elements before index i. For example, for array [1, 2, 3, 4], prefix_sum = [0, 1, 3, 6, 10].

Keywords: Subarray, Sum

When used with a hash map, make sure what to store as the key and value. The key could be prefix sum or its remainder over a number k, while the value could be the element index or the number of subarrays that have the same prefix sum.

Also remember to set a proper initial value for prefix_sum[0], which could be -1 in regard to index or 1 in regard to number of subarrays.

## Questions

- [Subarray Sum Equals K](subarray_sum.py)
- [Subarray Sums Divisible by K](subarray_sums_divisible_by_k.py)
- [Continuous Subarray Sum](continuous_subarray_sum.py)
- [Product of Array Except Self](product_of_array.py)
- [Continuous Subarray Sum](contiguous_array.py)
- [Minimum Size Subarray Sum](search/sliding_window/min_subarray.py)

## Reference

https://algo.monster/problems/subarray_sum

---

TODO:

- Range Sum
  - Matrix block sum
  - Range sum query 2D - Immutable
  - Range addition
- Sliding window
  - Maximum points you can obtain from cards
  - Minimum size array sum
- Monotonic queue
  - Shortest subaaray with sum at least k

Definition: prefix sum array has one more element prefix_sum[0] = 0

Sum equals k:

1. Find index: value is index in hash map
2. Find total: value is frequency in hash map

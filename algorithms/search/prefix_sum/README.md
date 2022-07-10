# 前缀和

- [和为 k 的子数组（整数数组）](subarray_sum.py)
- [连续的子数组和](continuous_subarray_sum.py)
- [连续数组](contiguous_array.py)
- [和可被 k 整除的子数组](subarray_sums_divisible_by_k.py)
- [长度最小的子数组（正整数数组）](search/sliding_window/min_subarray.py)
- 参考[前缀和专题](https://lucifer.ren/leetcode/thinkings/prefix.html)
- [除自身以外数组的乘积](product_of_array.py)：简化版本接雨水

前缀和是一种重要的预处理，能大大降低查询的时间复杂度。

关键词：连续、子数组

相关公式：

- `prefix_sums[i] = prefix_sums[i-1] + nums[i]`
- `subarray_sums[i-j] = prefix_sums[j] - prefix_sums[i-1]`

思路：

- 哈希表中存储的 key 和 value 是什么，前者可能是和或余数，后者可能是数量或下标。
- 预先在哈希表中设置 0 的初始值。
- 如果返回值是数量，则 value 一般是数量；如果返回值是长度，则 value 保存下标。

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

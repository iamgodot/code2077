# 给定一个含有 n 个正整数的数组和一个正整数 target 。
# 找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。


# 1. Brute force 双层 for 循环，时间复杂度 O(n^2)
# 2. 因为数组中都是正数，所以在外层 for 循环中可以使用前缀和进行二分查找，时间复杂度 O(n*logn)
# 3. 同样因为数组中都是正数，所以可以应用滑动窗口，时间复杂度 O(n)
def min_subarray_len(target: int, nums: list) -> int:
    length = len(nums)
    res = length + 1
    total = left = right = 0

    while right < length:
        total += nums[right]
        while total >= target:
            res = min(res, right - left + 1)
            total -= nums[left]
            left += 1
        right += 1

    return 0 if res == length + 1 else res


if __name__ == "__main__":
    assert min_subarray_len(1, []) == 0
    assert min_subarray_len(7, [2, 3, 1, 2, 4, 3]) == 2
    assert min_subarray_len(4, [1, 4, 4]) == 1
    assert min_subarray_len(11, [1, 2, 3, 4, 5]) == 3
    assert min_subarray_len(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
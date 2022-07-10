# 给定一个整数数组 nums 和一个整数 k ，返回其中元素之和可被 k 整除的（连续、非空） 子数组 的数目。
# 子数组 是数组的 连续 部分。

from typing import List


def find_subarrays(nums: List[int], k: int) -> int:
    """
    可被 k 整除也就是对 k 的余数相等。
    Time: O(n)
    Space: O(min(n, k))
    """
    from collections import defaultdict

    hashtable = defaultdict(int)
    hashtable[0] = 1
    res = remain = 0
    for num in nums:
        remain = (remain + num) % k
        res += hashtable.get(remain, 0)
        hashtable[remain] += 1
    return res


if __name__ == "__main__":
    assert find_subarrays([4, 5, 0, -2, -3, 1], 5) == 7
    assert find_subarrays([5], 9) == 0

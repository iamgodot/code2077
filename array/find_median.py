# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。


def find_median(nums1: list, nums2: list) -> float:
    # 中位数对于奇数个数来说是中间的那个数，对于偶数个数来说是中间两个数的平均值

    # 可以想象成分别把两个数组划分成左右两部分，如果有奇数个就在左边多放一个
    # 假设左边有 i 个元素，则左边部分的下标是 0, i-1，右边部分是 i, length-1
    # 如果两个数组都划分两部分之后，两个左边部分的最大值都小于两个右边部分的最小值，那么再保证两左的长度等于两右的长度就说明找到了中位数，即 i 和 j
    # i（或者说 j）的取值一开始肯定在中间，如果不符合比较条件就要移动：比如 nums1[i-1] > nums2[j] 就要把 i 左移，否则就右移
    # 这里要注意不是每次左移或者右移一位，而是类似二分查找的方式变换位置，才会得到 O(logn) 的复杂度
    # 另外 i 和 j 还存在一个等式关系，这样 i 的值变化了才能够对应到 j 的取值。
    # 这个关系来自于 i, j 的和应当等于 (m+n)/2 或者 (m+n)/2+1，合并起来就是等于 (m+n+1)/2，m, n 分别是两个数组的长度。

    # 解决了基本思路之后，还要考虑两个问题：
    # 1. 中位数的计算
    # 首先看对于普通情况来说，找到了 i, j 之后怎么计算中位数
    # 此时可以获得两个值，两左的最大值 max(nums1[i-1], nums2[j-1])，两右的最小值 min(nums1[i], nums2[j])
    # 因为左边会多放一个，所以奇数的话中位数就是两左的最大值，偶数的话就是两者的平均值
    # 2. 边界条件，也就是 i/j 等于 0 或者 length 的时候
    # 对 nums1 来说，如果 i=0，说明左边部分为空，此时左边的最大值 nums1[i-1] 就应当置为无限小，因为没有元素可以贡献
    # 如果 i=length，说明右边部分为空，此时右边的最小值就应当置为无限大，同样因为没有元素可以贡献。
    # 对 nums2 和 j 来说是同样的道理。
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)
    left, right = 0, m
    total_left = (m + n + 1) // 2
    while left < right:
        i = left + (right - left + 1) // 2  # 因为奇数个就在左边多放一个，所以 i 要偏大
        j = total_left - i
        if nums1[i - 1] > nums2[j]:
            right = i - 1
        else:
            left = i

    i, j = left, total_left - left
    first_left_max = nums1[i - 1] if i > 0 else -float("inf")
    first_right_min = nums1[i] if i < m else float("inf")
    second_left_max = nums2[j - 1] if j > 0 else -float("inf")
    second_right_min = nums2[j] if j < n else float("inf")

    if (m + n) % 2 == 1:
        return max(first_left_max, second_left_max)
    else:
        return (
            max(first_left_max, second_left_max)
            + min(first_right_min, second_right_min)
        ) / 2


# 将此题目泛化为寻找第 k 大的数字，不断比较两个数列 k/2 的位置的元素，然后排除掉较小的元素及其之前的部分
# 时间复杂度为 O(m+n)，虽然不是最优解，但是一个更普适的方案
def find_median(nums1, nums2):
    def find_kth_element(k, nums1, nums2):
        m, n = len(nums1), len(nums2)
        start1, start2 = 0, 0
        while True:
            if start1 == m:
                return nums2[start2 + k - 1]
            if start2 == n:
                return nums1[start1 + k - 1]
            if k == 1:
                return min(nums1[start1], nums2[start2])
            i = min(start1 + k // 2 - 1, m - 1)
            j = min(start2 + k // 2 - 1, n - 1)
            if nums1[i] <= nums2[j]:
                k -= i - start1 + 1
                start1 = i + 1
            else:
                k -= j - start2 + 1
                start2 = j + 1

    length = len(nums1) + len(nums2)
    if length % 2 == 1:
        return find_kth_element(length // 2 + 1, nums1, nums2)
    else:
        return (
            find_kth_element(length // 2, nums1, nums2)
            + find_kth_element(length // 2 + 1, nums1, nums2)
        ) / 2


if __name__ == "__main__":
    assert find_median([1, 3], [2]) == 2
    assert find_median([1, 2], [3, 4]) == 2.5
    assert find_median([0, 0], [0, 0]) == 0
    assert find_median([], [1]) == 1
    assert find_median([2], []) == 2

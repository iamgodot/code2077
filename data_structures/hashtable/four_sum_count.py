# 给定四个包含整数的数组列表 A , B , C , D
# 计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。
# 为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。
# 所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。


# 因为两层的嵌套循环，所以时间复杂度为 O(n^2)
# 空间复杂度在最坏情况下同样为 O(n^2)
def four_sum_count(nums1, nums2, nums3, nums4) -> int:
    from collections import Counter
    counter = Counter(m + n for m in nums1 for n in nums2)
    res = 0

    for i in nums3:
        for j in nums4:
            if -(i + j) in counter:
                res += counter[-(i + j)]

    return res


if __name__ == '__main__':
    assert four_sum_count([1, 2], [-2, -1], [-1, 2], [0, 2]) == 2
    assert four_sum_count([-1, -1], [-1, 1], [-1, 1], [1, -1]) == 6

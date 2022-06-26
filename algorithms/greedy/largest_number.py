# 给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
# 注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。


from functools import cmp_to_key
from typing import List


def largest_number(nums: List[int]) -> str:
    """
    需要证明：如果排序比较 a 优于 b 而 b 优于 c，则 a 优于 c

    时间复杂度：O(nlognlogm)，其中 nn 是给定序列的长度，mm 是 3232 位整数的最大值，每个数转化为字符串后的长度是 O(\log m)O(logm) 的数量级。
    空间复杂度：O(log n)O(logn)，排序需要 O(log n)O(logn) 的栈空间。

    Edge cases:
        数字可以重复并且可能为 0，所以要单独判断 [0...0] 这种全部多 0 的情况。

    """

    def compare(m: str, n: str) -> bool:
        if len(m) > len(n):
            return compare(n, m) * -1
        i = j = 0
        while i < len(m) and j < len(n):
            if m[i] == n[j]:
                i, j = i + 1, j + 1
                continue
            return 1 if m[i] > n[j] else -1

        if j == len(n):
            return 0

        return -1 if n[j] >= n[j - 1] else 1

    nums_sorted = sorted(
        [str(num) for num in nums], key=cmp_to_key(compare), reverse=True
    )
    return "".join(nums_sorted)


if __name__ == "__main__":
    assert largest_number([10, 2]) == "210"
    assert largest_number([3, 30, 34, 5, 9]) == "9534330"

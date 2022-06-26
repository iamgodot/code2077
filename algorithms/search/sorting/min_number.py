# 输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

from functools import cmp_to_key
from typing import List


# 核心思路比较简单，主要要想到两个数字如何做比较，也就是直接拼接成字符串再对比
# 时间复杂度 O(n*logn) 空间复杂度 O(n) 因为用到了额外的 strs 列表
def min_number(nums: List[int]) -> str:
    def compare(m, n):
        x, y = str(m), str(n)
        if x + y > y + x:
            return 1
        elif x + y < y + x:
            return -1
        else:
            return 0

    strs = [str(i) for i in nums]
    strs.sort(key=cmp_to_key(compare))
    return "".join(strs)


if __name__ == "__main__":
    assert min_number([10, 2]) == "102"
    assert min_number([3, 30, 34, 5, 9]) == "3033459"

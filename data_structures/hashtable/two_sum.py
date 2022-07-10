# 给定数字数组和一个目标整数，在数组中找到和为目标值的两个数字，并返回下标。
# 重点是答案里不能是同一个元素，所以要考虑目标值是某个数字两倍的情况。


from typing import List


def two_sum(nums: list, target: int) -> list:
    """
    使用哈希表将嵌套遍历优化为单次遍历：

    可以先遍历数组构造哈希表，然后再次遍历查找。在第一次遍历的时候对重复数字直接替换，这样也可以避免答案中出现同一个元素。

    更好的做法是只遍历一次，过程中先检查哈希表中有没有可用的答案，如果没有再将该元素更新到哈希表中，从而解决了重复元素的问题。

    Time: O(n)
    Space: O(n)
    """
    hash_table = {}

    for i, val in enumerate(nums):
        remain = target - val

        if remain in hash_table:
            return [hash_table[remain], i]
        hash_table[val] = i

    return []


# 给你一个下标从 1 开始的整数数组 numbers ，该数组已按 非递减顺序排列  ，请你从数组中找出满足相加之和等于目标数 target 的两个数。如果设这两个数分别是 numbers[index1] 和 numbers[index2] ，则 1 <= index1 < index2 <= numbers.length 。
# 以长度为 2 的整数数组 [index1, index2] 的形式返回这两个整数的下标 index1 和 index2。
# 你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。
# 你所设计的解决方案必须只使用常量级的额外空间。


def two_sum2(numbers: List[int], target: int) -> List[int]:
    i, j = 0, len(numbers) - 1
    while i < j:
        total = numbers[i] + numbers[j]
        if total == target:
            return [i + 1, j + 1]
        elif total < target:
            i += 1
        else:
            j -= 1
    return [-1, -1]


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum2([2, 7, 11, 15], 9) == [1, 2]

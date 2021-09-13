# 给定数字数组和一个目标整数，在数组中找到和为目标值的两个数字，并返回下标。
# 重点是答案里不能是同一个元素，所以要考虑目标值是某个数字两倍的情况。


# 1. Brute Force, O(n^2) & O(1)
def two_sum(nums: list, target: int) -> list:
    '''记得循环下标而不是数组本身。'''
    length = len(nums)

    for i in range(length):
        for j in range(i + 1, length):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []


# 2. Use hashtable, O(n) & O(n)
def two_sum_advanced(nums: list, target: int) -> list:
    '''
    使用哈希表将嵌套遍历优化为单次遍历：

    可以先遍历数组构造哈希表，然后再次遍历查找。在第一次遍历的时候对重复数字直接替换，这样也可以避免答案中出现同一个元素。

    更好的做法是只遍历一次，过程中先检查哈希表中有没有可用的答案，如果没有再将该元素更新到哈希表中，从而解决了重复元素的问题。
    '''
    hash_table = dict()

    for i, val in enumerate(nums):
        remain = target - val

        if remain in hash_table:
            return [hash_table[remain], i]
        hash_table[val] = i

    return []


if __name__ == '__main__':
    nums, target = [2, 7, 11, 15], 9
    assert two_sum(nums, target) == two_sum_advanced(nums, target) == [0, 1]

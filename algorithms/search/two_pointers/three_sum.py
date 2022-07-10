# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
# 使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。


def three_sum(nums: list) -> list:
    """
    类似 two_sum 但是必须要先对数组排序，
    在外层的遍历下再使用两端双指针，注意元素是可能重复的。

    时间复杂度 O(n^2) 其中还包括排序的 O(n*logn)
    空间复杂度 O(n) 因为改变了原有数组的顺序，排序也会耗费 O(logn)
    """
    nums.sort()
    res = []
    length = len(nums)

    for k in range(length):
        if k > 0 and nums[k] == nums[k - 1]:
            continue
        i, j = k + 1, length - 1

        while i < j:
            total = nums[k] + nums[i] + nums[j]
            if total < 0:
                i += 1
                while i < j and nums[i] == nums[i - 1]:
                    i += 1
            elif total > 0:
                j -= 1
                while i < j and nums[j] == nums[j + 1]:
                    j -= 1
            else:
                res.append([nums[k], nums[i], nums[j]])
                i += 1
                j -= 1
                while i < j and nums[i] == nums[i - 1]:
                    i += 1
                while i < j and nums[j] == nums[j + 1]:
                    j -= 1
    return res


if __name__ == "__main__":
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert three_sum([]) == []
    assert three_sum([0]) == []

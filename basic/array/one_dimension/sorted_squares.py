# 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。


# 1. Brute force 构造好平方数组后再排序，时间复杂度 O(logn)
# 2. 首尾双指针，时间复杂度 O(n)
def sorted_squares(nums: list) -> list:
    res = []
    left, right = 0, len(nums) - 1

    while left <= right:
        i, j = abs(nums[left]), abs(nums[right])

        if i > j:
            res.append(i**2)
            left += 1
        else:
            res.append(j**2)
            right -= 1

    return sorted(res)


if __name__ == '__main__':
    assert sorted_squares([]) == []
    assert sorted_squares([0]) == [0]
    assert sorted_squares([0, 1]) == [0, 1]
    assert sorted_squares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert sorted_squares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]

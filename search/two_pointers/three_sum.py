# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
# 使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。


# 类似 two_sum 但是必须要先对数组排序
# 在外层的遍历下再使用两端双指针，注意元素是可能重复的
# 时间复杂度 O(n^2) 其中还包括排序的 O(n*logn)
# 空间复杂度 O(n) 因为改变了原有数组的顺序
def three_sum(nums: list) -> list:
    nums.sort()
    res = []
    length = len(nums)

    for i in range(length):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        first = nums[i]
        left, right = i + 1, length - 1

        while left < right:
            three_sum = first + nums[left] + nums[right]

            if three_sum > 0:
                right -= 1
            elif three_sum < 0:
                left += 1
            else:
                res.append([first, nums[left], nums[right]])
                left += 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                right -= 1

                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return res


if __name__ == "__main__":
    print(three_sum([-1, 0, 1, 2, -1, -4]))
    print(three_sum([]))
    print(three_sum([0]))

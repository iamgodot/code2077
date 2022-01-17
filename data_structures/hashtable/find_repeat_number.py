# 找出数组中重复的数字。
# 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

# 1. BruteForce: 双层遍历，最坏时间复杂度 O(n^2)
# 2. 排序：时间复杂度 O(n*logn)
# 3. 哈希表：时间复杂度 O(n) 空间复杂度 O(n)
def find_repeat_number(nums: list) -> int:
    s = set()
    for num in nums:
        if num in s:
            return num
        s.add(num)


# 4. 利用数组索引：时间复杂度 O(n) 空间复杂度 O(1)
def find_repeat_number2(nums: list) -> int:
    index = 0
    while index < len(nums):
        if index == nums[index]:
            index += 1
            continue
        if nums[index] == nums[nums[index]]:
            return nums[index]
        else:
            # 注意这里不能把 nums[index] 放在前面，因为赋值是准备好右边，
            # 再对左边进行从左到右的更新，如果 nums[index] 先更新，那么
            # nums[nums[index]] 就不对了
            nums[nums[index]], nums[index] = nums[index], nums[nums[index]]

# 给定一个包含 n + 1 个整数的数组 nums ，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。
# 假设 nums 只有 一个重复的整数 ，找出 这个重复的数 。
# 你设计的解决方案必须不修改数组 nums 且只用常量级 O(1) 的额外空间。


# 注意根据题意，数组中只有一个重复的整数，但是有可能重复任意次
# 使用二分查找的前提是有序数组 + 单调条件
# 这里对于数组 1-n 进行二分，条件是对于其中一个元素，nums 中小于等于该元素的数字总数 count
# 在 [1, target-1] 中是 count <= num，在 [target, n] 中是 count > num 的
# 二分的时间复杂度是 O(n*logn)，其中 n 是 count 带来的成本
# 另外还可以考虑位运算，计算每一位的重复，最后时间复杂度也是 O(n*logn)
def find_duplicate1(nums: list) -> int:
    dup = 0
    left, right = 1, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        count = len([num for num in nums if num <= mid])
        if count <= mid:
            left = mid + 1
        else:
            right = mid - 1

    return left


# 从 0 开始，把数组模拟成 n -> nums[n] 的链表，重复数字会在链表中制造环
# 判断是否存在重复数字就相当于判断是否有环
# 找重复数字相当于找出环的入口
# 时间复杂度 O(n)
def find_duplicate2(nums: list) -> int:
    slow = fast = nums[0]

    while True:
        slow, fast = nums[slow], nums[nums[fast]]

        if slow == fast:
            slow = nums[0]
            while slow != fast:
                slow, fast = nums[slow], nums[fast]
            return slow


if __name__ == "__main__":
    for method in find_duplicate1, find_duplicate2:
        assert method([1, 3, 4, 2, 2]) == 2
        assert method([3, 1, 3, 4, 2]) == 3

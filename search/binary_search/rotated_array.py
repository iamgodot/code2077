# 已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,4,4,5,6,7] 在变化后可能得到：
# 若旋转 4 次，则可以得到 [4,5,6,7,0,1,4]
# 若旋转 7 次，则可以得到 [0,1,4,4,5,6,7]
# 注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。

# 给你一个可能存在 重复 元素值的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。


# 通过二分法来比较中间元素与末尾元素的大小
# 时间复杂度 O(logn) 最坏情况下会达到 O(n)
def find_min(nums: list) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) >> 1
        if nums[mid] > nums[right]:
            left = mid + 1
        elif nums[mid] < nums[right]:
            right = mid  # 这里不能排除掉 mid 元素
        else:
            # 其实可以从 right 开始往左排除相同元素，一直到 mid
            right -= 1  # mid 与 right 元素相同，所以去掉也没关系

    # 关于为什么要返回 `numbers[left]`: 因为二分循环到最后 left 和 right 都会聚合到旋转点上，此时再一次循环就会执行 `right -= 1`，因为判断肯定相等。那么 left 就会留在旋转点上，而 right 跑到了 left 左边。
    return nums[left]


if __name__ == "__main__":
    assert find_min([1, 3, 5]) == 1
    assert find_min([2, 2, 2, 0, 1]) == 0

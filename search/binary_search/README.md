# 二分查找

二分查找的前提是有序序列，可以达到 O(logn) 的时间复杂度。

大体上可以分为两种类型：三分和两分。

## 三分

也就是最常见的二分实现，三分表示将序列分为左半、中间元素和右半三部分。

```python
def bs(nums: list, target: int) -> int:
    res = -1
    left, right = 0, len(nums) - 1

    while left <= right:
        # 这里为了防止溢出应当写成 left + (right-left)//2
        # 但是 Python 会在内存中模拟大数运算所以不用这么做
        # 对于偶数序列会选择偏左的元素
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return res
```

这种写法对于重复元素的情况可以找到合法结果，但具体是哪一个是不确定的。

## 两分

参考 https://leetcode-cn.com/problems/binary-search/solution/er-fen-cha-zhao-xiang-jie-by-labuladong/

- bisect left
  - left 依然取 0，但是 right 要取 len(nums) 而不是 len(nums) - 1。
  - while 条件没有等于号，因为用的是左闭右开的区间。
  - left = mid + 1，right = mid，这跟 bisect left 还是 right 没有关系，是由遵循左开右闭决定的。
  - 因为 bisect left 所以 nums[mid] == target 时要 right = mid 继续往左查看。
  - 找到的结果 i 是多个 target 最左边那个的下标。[1,1,2] 如果找 1 的话结果为 0，相当于左边的闭边界。
  - 如果不存在，则找应当插入的位置。[1,1,2] 如果 bisect_left 0 的话结果为 0，3 的话结果为 3。
- bisect right
  - nums[mid] == target 时要 left = mid + 1 继续向右查看。
  - 找到的结果 i 是多个 target 最右边那个的下标 + 1。[1,1,2] 如果找 1 的话结果为 2，相当于右边的开边界。
  - 如果不存在，也是找应当插入的位置。[1,1,2] 如果找 0 的话结果为 0，3 的话结果为 3。

bisect right 的话 python 的实现版本是返回 index + 1，也就是 return left，如果要 index 的话就应当是 return left - 1。

重点就是左开右闭，所以 right 取值 + while 条件 + left/right 更新 + return 结果都要对应。

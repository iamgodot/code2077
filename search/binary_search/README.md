# 二分查找

二分查找的前提是有序序列，通过每次折半可以达到 O(logn) 的时间复杂度。

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

这种情况针对的是寻找边界元素，而不是特定值的元素的位置。

- 右侧边界：使用 `value <= target` 条件搜索，因为 target 在右边，所以是右界，搜索结束后，left 是右侧外界，也就是 `nums[left] > target`，right 在 left 左边，也就是右侧内界
- 左侧边界：同右侧边界正好相反，搜索结束后，right 是左侧外界

另外对于没有等号的情况，比如 `value > target`，实际上是找左侧边界，实现上等价于上面右侧外界的情况，此时 left 为左侧内界，而 right 为左侧外界。

```python
def search(nums: list, target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1

    return left
```

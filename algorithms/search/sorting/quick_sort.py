# 快速排序是一种利用了分治法 Divide and Conquer 的排序思路
from random import randint


def quick_sort(nums: list, left: int, right: int) -> None:
    """直接指定最左边下标为 pivot."""

    if left >= right:
        return

    pivot, i, j = left, left, right

    # 随机交换来避免最差情况的时间复杂度
    index_random = randint(left + 1, right)
    nums[pivot], nums[index_random] = nums[index_random], nums[pivot]

    while i < j:
        # 先移动 j 的原因是 pivot 默认在左
        # 如果先移动 i 可能会造成 pivot 元素被交换到较大序列
        # 而一个较大元素被放到 pivot 位置，即在较小序列里面

        while nums[j] >= nums[pivot] and i < j:
            j -= 1

        while nums[i] <= nums[pivot] and i < j:
            i += 1

        nums[i], nums[j] = nums[j], nums[i]

    nums[pivot], nums[i] = nums[i], nums[pivot]
    quick_sort(nums, left, i - 1)
    quick_sort(nums, i + 1, right)


def quick_sort_with_stack(nums: list, left: int, right: int) -> None:
    """使用堆栈替代递归。"""
    stack = []

    while left < right or stack:
        if left < right:
            pivot, i, j = left, left, right

            index_random = randint(left + 1, right)
            nums[pivot], nums[index_random] = nums[index_random], nums[pivot]

            while i < j:
                while nums[j] >= nums[pivot] and i < j:
                    j -= 1

                while nums[i] <= nums[pivot] and i < j:
                    i += 1

                nums[i], nums[j] = nums[j], nums[i]

            nums[pivot], nums[i] = nums[i], nums[pivot]
            stack.append([i + 1, right])
            right = i - 1
        else:
            left, right = stack.pop()


if __name__ == "__main__":
    for sort_method in [quick_sort, quick_sort_with_stack]:
        nums = [5, 8, 6, 3, 9, 2, 1, 7, 4]
        sort_method(nums, 0, len(nums) - 1)
        assert nums == [i for i in range(1, 10)]

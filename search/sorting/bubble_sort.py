# 冒泡排序是一种简单的交换排序，也是一种稳定的排序方法


def bubble_sort(nums: list) -> list:
    '''一共两层嵌套循环，外层循环 n-1 次，有序区从右侧开始延伸至左。'''
    length = len(nums)

    for i in range(length - 1):
        for j in range(length - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


def bubble_sort_with_flag(nums: list) -> list:
    '''通过设置 flag 减少不必要的循环。'''
    length = len(nums)

    for i in range(length - 1):
        is_sorted = True

        for j in range(length - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                is_sorted = False

        if is_sorted:
            break

    return nums


def bubble_sort_with_flag_and_pos(nums: list) -> list:
    '''通过设置 pos 进一步减少循环的长度。'''
    length = len(nums)
    pos = length - 1

    for i in range(length - 1):
        is_sorted = True

        for j in range(pos):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                is_sorted = False
                pos = j

        if is_sorted:
            break

    return nums


def cocktail_sort(nums: list) -> list:
    '''鸡尾酒排序，每次冒泡都更改方向，也就是双向冒泡。对于小数在右的情况，可以大大减少排序的回合。'''
    length = len(nums)

    for i in range(length // 2):
        is_sorted = True

        for j in range(length - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                is_sorted = False

        if is_sorted:
            break
        is_sorted = True

        for j in range(length - 1, i, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                is_sorted = False

        if is_sorted:
            break

    return nums


if __name__ == '__main__':
    for sort_method in [
            bubble_sort, bubble_sort_with_flag, bubble_sort_with_flag_and_pos,
            cocktail_sort
    ]:
        nums = [5, 8, 6, 3, 9, 2, 1, 7, 4]
        print(sort_method(nums))

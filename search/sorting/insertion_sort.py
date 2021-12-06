def insertion_sort(nums: list) -> list:
    for i in range(1, len(nums)):
        val, pos = nums[i], i - 1

        while pos >= 0 and nums[pos] > val:
            nums[pos + 1] = nums[pos]
            pos -= 1

        nums[pos + 1] = val

    return nums


if __name__ == '__main__':
    nums = [5, 8, 6, 3, 9, 2, 1, 7, 4]
    print(insertion_sort(nums))

from random import randint


def quick_select(nums: list, left: int, right: int, k: int) -> int:
    """
    Time: O(n) in worst case O(n^2)
    Space: O(logn) in worst case O(n)
    """
    if left >= right:
        return nums[left]

    pivot, i, j = left, left, right

    index_random = randint(left + 1, right)
    nums[pivot], nums[index_random] = nums[index_random], nums[pivot]

    while i < j:
        while i < j and nums[j] >= nums[pivot]:
            j -= 1
        while i < j and nums[i] <= nums[pivot]:
            i += 1
        nums[i], nums[j] = nums[j], nums[i]

    nums[pivot], nums[i] = nums[i], nums[pivot]
    # 如果是求第 k 小，则 index = k - 1
    index = len(nums) - k
    if i == index:
        return nums[i]
    elif i > index:
        return quick_select(nums, 0, i - 1, k)
    else:
        return quick_select(nums, i + 1, right, k)


def find_kth_largest(nums: list, k: int) -> int:
    # return quick_sort(nums, 0, len(nums) - 1, k)
    import heapq

    hq = []
    for num in nums:
        if len(hq) == k:
            heapq.heappushpop(hq, num)
            continue
        heapq.heappush(hq, num)

    return heapq.heappop(hq)


if __name__ == "__main__":
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert find_kth_largest([1], 1) == 1

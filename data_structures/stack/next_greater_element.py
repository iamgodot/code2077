# Next Greater Element I
# https://leetcode.com/problems/next-greater-element-i/description


def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    Use a mono stack, we don't need to worry about duplicates here(otherwise there could be collisions in the hashtable).

    Time: O(m+n) m as len(nums2), n as len(nums1)
    Space: O(m)
    """
    stack, hashtable = [], {}
    length = len(nums2)
    for i in range(length - 1, -1, -1):
        num = nums2[i]
        while stack and stack[-1] <= num:
            stack.pop()
        if stack:
            hashtable[num] = stack[-1]
        stack.append(num)
    return [hashtable.get(i, -1) for i in nums1]


# Next Greater Element II
# https://leetcode.com/problems/next-greater-element-ii/description


def next_greater_element2(nums: list[int]) -> list[int]:
    """
    Same as above, but we use twice the length to simulate the expansion of the array.
    """
    length = len(nums)
    stack, res = [], [-1 for _ in range(length)]
    for i in range(2 * length - 1, -1, -1):
        num = nums[i % length]
        while stack and stack[-1] <= num:
            stack.pop()
        if stack:
            res[i % length] = stack[-1]
        stack.append(num)
    return res


if __name__ == "__main__":
    assert next_greater_element([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]
    assert next_greater_element([2, 4], [1, 2, 3, 4]) == [3, -1]
    assert next_greater_element2([1, 2, 1]) == [2, -1, 2]
    assert next_greater_element2([1, 2, 3, 4, 3]) == [2, 3, 4, -1, 4]

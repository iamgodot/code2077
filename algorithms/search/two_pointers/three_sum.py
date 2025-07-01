# 3Sum
# https://leetcode.com/problems/3sum/


def three_sum(nums: list) -> list:
    """
    1. Use two pointers, remember to sort first.

    Time: O(n^2)
    Space: O(logn) or O(n) depending on the sorting algorithm

    2. Use a hashset to find the remaining 2 numbers(still need to sort),
    don't need hash table since we're returning values rather than indices.

    Time: O(n^2)
    Space: O(n) for both the hashset and sorting

    3. Use 2 hashsets without sorting.

    Time: O(n^2) while hashset lookups are more expensive
    Space: O(n), or it could be O(n^2) for worst cases
    """
    nums_sorted = sorted(nums)
    res = []
    length = len(nums_sorted)

    for k in range(length - 2):
        if k > 0 and nums_sorted[k] == nums_sorted[k - 1]:
            continue
        i, j = k + 1, length - 1

        while i < j:
            total = nums_sorted[k] + nums_sorted[i] + nums_sorted[j]
            if total < 0:
                i += 1
            elif total > 0:
                j -= 1
            else:
                res.append([nums_sorted[i], nums_sorted[i], nums_sorted[j]])
                i += 1
                j -= 1
                while i < j and nums_sorted[i] == nums_sorted[i - 1]:
                    i += 1
                while i < j and nums_sorted[j] == nums_sorted[j + 1]:
                    j -= 1


# TODO: 3Sum Closest
# https://leetcode.com/problems/3sum-closest/description/

# TODO: 3Sum Smaller
# https://leetcode.com/problems/3sum-smaller/description/


def fourSum(nums: list[int], target: int) -> list[list[int]]:
    """
    For k sum:
    Time: O(n^(k-1))
    Space: O(n)
    """

    def k_sum(nums, target, k):
        res = []
        if not nums:
            return res
        if k == 2:
            return two_sum(nums, target)

        for i in range(len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                for subset in k_sum(nums[i + 1 :], target - nums[i], k - 1):
                    res.append([nums[i]] + subset)
        return res

    def two_sum(nums, target):
        res = []
        left, right = 0, len(nums) - 1
        while left < right:
            sum_ = nums[left] + nums[right]
            if sum_ < target:
                left += 1
            elif sum_ > target:
                right -= 1
            else:
                res.append([nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
        return res

    nums.sort()
    return k_sum(nums, target, 4)


if __name__ == "__main__":
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert three_sum([]) == []
    assert three_sum([0]) == []

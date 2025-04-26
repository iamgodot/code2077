# Two Sum
# https://leetcode.com/problems/two-sum/


def two_sum(nums: list, target: int) -> list:
    """
    Time: O(n)
    Space: O(n)
    """
    hash_table = {}

    for i, val in enumerate(nums):
        remain = target - val

        if remain in hash_table:
            return [hash_table[remain], i]
        hash_table[val] = i

    return []


# Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/


def two_sum2(numbers: list[int], target: int) -> list[int]:
    i, j = 0, len(numbers) - 1
    while i < j:
        total = numbers[i] + numbers[j]
        if total == target:
            return [i + 1, j + 1]
        elif total < target:
            i += 1
        else:
            j -= 1
    return [-1, -1]


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum2([2, 7, 11, 15], 9) == [1, 2]

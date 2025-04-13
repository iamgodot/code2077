# Permutations
# https://leetcode.com/problems/permutations/description/


def permute(nums: list) -> list:
    """
    Time: O(n*n!)
    Space: O(n) for the recursive stack
    """
    res, path = [], []

    def bt():
        if len(path) == len(nums):
            res.append(path.copy())
            return
        for num in nums:
            if num not in path:
                path.append(num)
                bt()
                path.pop()

    bt()
    return res


# Permutations II
# https://leetcode.com/problems/permutations-ii/description/


def permute_unique(nums: list) -> list:
    """
    Time: O(n*n!)
    Space: O(n) for the recursive stack
    """
    length = len(nums)
    res, path = [], []
    used = [0 for _ in range(length)]

    def bt():
        if len(path) == length:
            res.append(path.copy())
            return
        for i in range(length):
            if used[i]:
                continue
            # NOTE: here if element i-1 is not used, meaning this kind of
            # permutation is explored, so we can skip it
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue
            path.append(nums[i])
            used[i] = 1
            bt()
            used[i] = 0
            path.pop()

    nums.sort()
    bt()
    return res


if __name__ == "__main__":
    assert permute([1, 2, 3]) == [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]
    assert permute([0, 1]) == [[0, 1], [1, 0]]
    assert permute([1]) == [[1]]
    assert permute_unique([1, 1, 2]) == [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
    assert permute_unique([1, 2, 3]) == [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]

# Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/


def subarray_sum(nums: list, k: int) -> int:
    """
    If asked to return the start and end index of the subarray, we need to use indices as the values in the hash map, which can be initialized as {0: 0}.

    Update hash map at the end of each iteration to avoid using the same element again, just as the case of 2sum.
    """

    from collections import defaultdict

    count = total = 0
    # NOTE: set value to 1 for prefix_sum[0] for cases of first n elements sum up to k
    hashtable = defaultdict(int, {total: 1})
    for num in nums:
        total += num
        count += hashtable[total - k]
        hashtable[total] += 1

    return count


if __name__ == "__main__":
    assert subarray_sum([1, 2, 3], 3) == 2
    assert subarray_sum([1], 0) == 0

# Continuous Subarray Sum
# https://leetcode.com/problems/continuous-subarray-sum/description/


def check(nums: list[int], k: int) -> bool:
    """
    Time: O(n)
    Space: O(min(n, k))
    """
    # NOTE: the sum remain of k: index
    # We need -1 to find out the subarray of size 2 from the first element
    hashtable = {0: -1}
    remain = 0
    for i in range(len(nums)):
        remain = (remain + nums[i]) % k
        if remain in hashtable:
            if i - hashtable[remain] > 1:
                return True
        else:
            hashtable[remain] = i
    return False


if __name__ == "__main__":
    assert check([23, 2, 4, 6, 7], 6) is True
    assert check([23, 2, 6, 4, 7], 13) is False

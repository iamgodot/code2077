# Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/


def product_except_self(nums: list[int]) -> list[int]:
    """
    Time: O(n)
    Space: O(1)
    """
    length = len(nums)
    res = [1] * length
    for i in range(1, length):
        res[i] = res[i - 1] * nums[i - 1]
    prod_r = 1
    print(res)
    for i in range(length - 1, -1, -1):
        res[i] *= prod_r
        prod_r *= nums[i]
    return res


if __name__ == "__main__":
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]

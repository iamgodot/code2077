# 给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。

# 1. 可以通过数学来求 nums 的和，然后再用 0-n 的和减去它
# 2. 也可以把 n 个数再加上 0-n 的 n+1 个数，再对这 2n+1 个数做异或
def find_missing_number(nums: list) -> int:
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)


# 如果有两个整数出现了奇数次，如何找出这两个整数

# 所有整数的异或结果相当于这两个整数的异或结果，根据此结果可以判断两个数是从二进制的
# 第几位开始不同的，通过这一位可以将所有的数分成两部分，每一部分各包含一个落单的整数
# 再分别异或即可
def find_missing_number2(nums: list) -> list:
    res = [0, 0]
    xor_res = 0
    for i in nums:
        xor_res ^= i
    separator = 1
    while xor_res & separator == 0:
        separator <<= 1
    for i in nums:
        if i & separator == 0:  # 注意这里的两种结果是 0/separator 而不是 0/1
            res[0] ^= i
        else:
            res[1] ^= i
    return res


# 在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。


# 思路是通过累加每一位二进制位的数字并做 3 的余数，结果就是只出现一次的数字
# 使用状态机可以实现，利用两位二进制数表达 0/1/2 三种余数
# 时间复杂度 O(n) 空间复杂度 O(1)
def single_number(nums: list) -> int:
    ones = twos = 0
    for num in nums:
        ones = ones ^ num & ~twos
        twos = twos ^ num & ~ones
    return ones


if __name__ == "__main__":
    assert find_missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    nums = [i for i in range(1, 100)] * 2 + [101, 102]
    assert sorted(find_missing_number2(nums)) == [101, 102]

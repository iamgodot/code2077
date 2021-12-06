# 在一个无序数组里有 99 个不重复的正整数，范围是 1~100，唯独缺少一个 1~100 中的整数
# 如何找出这个整数

# 可以先求出 1~100 的和，然后减去数组中的所有的数字，结果就是要找的整数了
def find_missing_number(nums: list) -> int:
    return sum(range(1, 101)) - sum(nums)


# 一个无序数组里面有若干个正整数，范围是 1~100，其中 99 个整数都出现了偶数次
# 只有一个整数出现了奇数次，如何找出这个整数

# 两个相同的数字的异或结果为 0，一个数字和 0 的异或结果为这个数字本身
# 所以直接把所有的元素都做一遍异或就可以得到落单的整数了
def find_missing_number2(nums: list) -> int:
    res = 0
    for i in nums:
        res ^= i

    return res


# 如果有两个整数出现了奇数次，如何找出这两个整数

# 所有整数的异或结果相当于这两个整数的异或结果，根据此结果可以判断两个数是从二进制的
# 第几位开始不同的，通过这一位可以将所有的数分成两部分，每一部分各包含一个落单的整数
# 再分别异或即可
def find_missing_number3(nums: list) -> list:
    res = [0, 0]
    xor_res = 0
    for i in nums:
        xor_res ^= i
    separator = 1
    while xor_res & separator == 0:
        separator <<= 1
    for i in nums:
        if i & separator == 0:
            res[0] ^= i
        else:
            res[1] ^= i
    return res


if __name__ == "__main__":
    nums = [i for i in range(1, 50)] + [i for i in range(51, 101)]
    assert find_missing_number(nums) == 50
    nums = [i for i in range(1, 100)] * 2 + [101]
    assert find_missing_number2(nums) == 101
    nums = [i for i in range(1, 100)] * 2 + [101, 102]
    assert sorted(find_missing_number3(nums)) == [101, 102]

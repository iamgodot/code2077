# 给你一个整数 n ，对于 0 <= i <= n 中的每个 i ，计算其二进制表示中 1 的个数 ，返回一个长度为 n + 1 的数组 ans 作为答案。


# 1. 对每个数进行 hamming 计算 1 的个数，时间复杂度 O(n*logn)
# 2. 对于奇数，1 的个数是前一个偶数加 1；对于偶数，1 的个数和其一半相同
# 如此动态规划下来，时间复杂度 O(n)
def count_bits(n: int) -> list:
    res = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        if i & 1 == 1:
            res[i] = res[i - 1] + 1
        else:
            res[i] = res[i // 2]
    return res


if __name__ == "__main__":
    assert count_bits(5) == [0, 1, 1, 2, 1, 2]

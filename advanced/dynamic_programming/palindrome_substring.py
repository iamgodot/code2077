# 给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。
# 回文字符串 是正着读和倒过来读一样的字符串。
# 子字符串 是字符串中的由连续字符组成的一个序列。
# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。


def count(s: str) -> int:
    """
    dp[i][j] 表示 s[i:j+1] 是否为回文字符串

    递推公式：
        if s[i] == s[j]:
            if j - i <= 1: True
            else: dp[i+1][j-1]

    初始化：全 False

    遍历顺序：左下 -> 右上 & j >= i

    时间复杂度 O(n^2) 空间复杂度 O(n^2)
    """
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    res = 0

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j]:
                if j - i <= 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i + 1][j - 1]
                res += dp[i][j]

    return res


def count2(s: str) -> int:
    """
    使用双指针中心扩展法，对于每一个字符，都有一个或两个字符为中心向外扩展的情况

    时间复杂度 O(n^2) 空间复杂度 O(1)
    """

    def extend(i, j) -> None:
        nonlocal result
        while i >= 0 and j < n and s[i] == s[j]:
            i -= 1
            j += 1
            result += 1

    n, result = len(s), 0
    for i in range(len(s)):
        extend(i, i)  # 以i为中心
        extend(i, i + 1)  # 以i和i+1为中心
    return result


# 给你一个字符串 s，找到 s 中最长的回文子串。


def longest(s: str) -> str:
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    res = ""

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j]:
                if j - i <= 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and j - i + 1 > len(res):
                    res = s[i : j + 1]
    return res


def longest2(s: str) -> int:
    def extend(i, j) -> None:
        nonlocal result
        while i >= 0 and j < n and s[i] == s[j]:
            if j - i + 1 > len(result):
                result = s[i : j + 1]
            i -= 1
            j += 1

    n, result = len(s), ""
    for i in range(len(s)):
        extend(i, i)  # 以i为中心
        extend(i, i + 1)  # 以i和i+1为中心
    return result


if __name__ == "__main__":
    for method in [count, count2]:
        assert method("abc") == 3
        assert method("aaa") == 6
    for method in [longest, longest2]:
        assert method("babad") in ["bab", "aba"]
        assert method("cbbd") == "bb"

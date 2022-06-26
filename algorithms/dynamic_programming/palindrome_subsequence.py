# 给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。
# 子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。


def longest(s: str) -> int:
    """
    dp[i][j] 表示 s[i:j+1] 中最长回文子序列的长度

    递推公式：
        if s[i] == s[j]: dp[i][j] = dp[i+1][j-1] + 2
        else: dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    初始化：
        对于 i == j: dp[i][j] = 1

    遍历顺序：左下 -> 右上 & j > i

    时间复杂度 O(n^2) 空间复杂度 O(n^2)
    """
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][-1]


if __name__ == "__main__":
    assert longest("bbbab") == 4
    assert longest("cbbd") == 2

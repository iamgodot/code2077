# 给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。

# 你可以对一个单词进行如下三种操作：

# 插入一个字符
# 删除一个字符
# 替换一个字符


def min_distance(word1: str, word2: str) -> int:
    """
    dp[i][j] 表示 word1 的前 i-1 个字符转换为 word2 的前 j-1 个字符的编辑距离。

    递推公式：
        if word1[i-1] == word2[j-1]: dp[i][j] = dp[i-1][j-1]
        else: dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

    初始化：
        dp[0][0..n] 表示空字符串转换为 word2 的前 j-1 个字符，结果为 j
        dp[0..m][0] 表示 word1 的前 i-1 个字符转换为空字符串，结果为 i
    """
    m, n = len(word1), len(word2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
    return dp[-1][-1]


if __name__ == "__main__":
    assert min_distance("horse", "ros") == 3
    assert min_distance("intention", "execution") == 5

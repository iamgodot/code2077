# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

# 子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。


def longest_increasing_subsequence(nums: list[int]) -> int:
    """
    dp[i] 表示以 i 为最后一个元素的数组，它的最长递增子序列的值
    dp[i] = max(dp[i], dp[j] + 1) 的意思是这个最长递增子序列的值
    如果 nums[i] > nums[j] 则取决于前面所有以 j 为最后一个元素的数组
    的最长递增子序列的长度加 1.

    初始化：每个位置的初始值都至少为 1.

    时间复杂度：O(n^2)
    空间复杂度：O(n)
    """
    length = len(nums)
    dp = [1 for _ in range(length)]
    for i in range(1, length):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


# 给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

# 一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
# 两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。


def longest_common_sequence(text1: str, text2: str) -> int:
    """
    dp[i][j] 表示 text1 的前 i-1 部分和 text2 的前 j-1 部分的最长公共子序列的长度。

    递推公式：
        if text1[i-1] == text2[j-1]: dp[i][j] = dp[i-1][j-1] + 1
        else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    初始化：
        dp[0][j] 和 dp[i][0] 都应当初始化为 0，因为空字符串无法匹配公共子序列。

    时间复杂度：O(m * n)
    空间复杂度：O(m * n)
    """
    m, n = len(text1), len(text2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    # 其实可以省略掉，这里为了体现初始化过程
    for i in range(1, m + 1):
        dp[i][0] = 0
    for j in range(1, n + 1):
        dp[0][j] = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]


# 给定一个未经排序的整数数组，找到最长且 连续递增的子序列，并返回该序列的长度。

# 连续递增的子序列 可以由两个下标 l 和 r（l < r）确定，如果对于每个 l <= i < r，都有 nums[i] < nums[i + 1] ，那么子序列 [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] 就是连续递增子序列。


def longest_continuous_increasing_subsequence(nums: list[int]) -> int:
    pre = res = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            pre += 1
            res = max(res, pre)
        else:
            pre = 1
    return res


# 给两个整数数组 nums1 和 nums2 ，返回 两个数组中 公共的 、长度最长的子数组的长度 。


def find_length(nums1: list[int], nums2: list[int]) -> int:
    """
    注意这里的子数组是连续的子序列。

    定义 dp[i][j] 为 nums1 的前 i-1 个元素和 nums2 的前 j-1 个元素的公共子数组最长长度。

    递推公式：
        if nums1[i-1] == nums2[j-1]: dp[i][j] = dp[i-1][j-1] + 1

    初始化：
        dp[0][j] 和 dp[i][0] 都应当初始化为 0，因为空数组匹配不到任何公共子数组。

    注意最后结果不是取 dp[-1][-1]，因为矩阵的更新只取决于左上方的值，所以 dp[-1][-1] 不一定是最大的。
    """
    m, n = len(nums1), len(nums2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    # 其实可以省略掉，这里为了体现初始化过程
    for i in range(1, m + 1):
        dp[i][0] = 0
    for j in range(1, n + 1):
        dp[0][j] = 0

    res = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if nums1[i - 1] == nums2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            res = max(res, dp[i][j])

    return res


# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
# 字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

# 进阶：
# 如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？


def is_subsequence(s: str, t: str) -> bool:
    """
    1. 双指针法，时间复杂度为 O(m + n) 其中 m 为 t 的长度，n 为 s 的长度。
    2. 二分查找：先对 t 进行预处理，哈希表存储其中字母对应所有出现位置的列表。之后再遍历 s 时，就可以对列表二分查找得到下一个匹配的位置。
        时间复杂度为 O(n * logm + n) -> O(n * logm) 空间复杂度为 O(n)
    3. 动态规划：dp[i][j] 表示 t 中从 i 位置开始字母 j 第一次出现的位置，那么如果 i 位置就是字母 j 则 dp[i][j] = i 否则 dp[i][j] = dp[i+1][j]
        初始化时第 m 行全部可以初始化为 m，表示从这行开始不存在字母 j（因为最后的有效行应为第 m-1 行）。
        时间复杂度为 O(m * 26 + n) 空间复杂度为 O(m * 26)

    如果有大量的 S 输入，则动态规划的时间效率会高很多，为 O(m * 26 + n * k) 而双指针法为 O(m * k + n * k)
    """
    i = j = 0
    while i < len(s) and j < len(t):
        c1, c2 = s[i], t[j]
        if c1 == c2:
            i += 1
        j += 1

    return i == len(s)


# 给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。
# 字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）
# 题目数据保证答案符合 32 位带符号整数范围。


def num_distinct(s: str, t: str) -> int:
    """
    dp[i][j] 表示 s 的前 i-1 个字符和 t 的前 j-1 个字符的匹配结果。

    递归公式：
        if s[i-1] == t[j-1]: dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        else: dp[i][j] = dp[i-1][j]

    初始化：
        dp[0][0] 表示空字符串匹配空字符串，结果为 1
        dp[1..m][0] 表示 s 匹配空字符串，结果为 1
        dp[0][1..n] 表示空字符串匹配 t，结果为 0
    """
    m, n = len(s), len(t)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    dp[0][0] = 1
    for i in range(1, m + 1):
        dp[i][0] = 1
    for j in range(1, n + 1):
        dp[0][j] = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[-1][-1]


if __name__ == "__main__":
    assert longest_increasing_subsequence([0, 1, 0, 3, 2]) == 3
    assert longest_common_sequence("abcde", "ace") == 3
    assert longest_continuous_increasing_subsequence([1, 3, 5, 4, 7]) == 3
    assert find_length([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]) == 3
    assert is_subsequence("abc", "ahbgdc") is True

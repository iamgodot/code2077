# Word Break
# https://leetcode.com/problems/word-break/


def wordBreak(s: str, wordDict: list[str]) -> bool:
    """
    Time: O(n*m*k) where n is the length of s, m is the length of wordDict and k is the average length of words.
    Space: O(n)
    """
    length = len(s)
    dp = [False] * (length + 1)
    dp[-1] = True
    for i in range(length - 1, -1, -1):
        for w in wordDict:
            length_word = len(w)
            if i + length_word <= length and s[i : i + length_word] == w:
                dp[i] = dp[i + length_word]
            if dp[i]:
                break
    return dp[0]

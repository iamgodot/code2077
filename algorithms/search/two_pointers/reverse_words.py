# 给你一个字符串 s ，逐个翻转字符串中的所有 单词 。


# 可以调用 API，也可以先全翻转再单个翻转，也可以用 deque. 复杂度都一样（对 Python 来说）
# 时间复杂度：O(n)
# 空间复杂度：O(n)
from typing import List


def reverse_words(s: str):
    # return  ' '.join(s.split()[::-1])
    from collections import deque

    words = deque()
    word = ""
    for char in s:
        if char == " " and word:
            words.appendleft(word)
            word = ""
        elif char != " ":
            word += char
    else:
        if word:
            words.appendleft(word)

    return " ".join(words)


def reverse_words2(s: str):
    """
    Time: O(n)
    Space: O(1)
    """

    def trim(string: str) -> List[str]:
        """
        注意 strip 两边的空格，同时每个单词之间只保留一个空格。
        """
        chars = []
        left, right = 0, len(string) - 1
        while left <= right and string[left] == " ":
            left += 1
        while left <= right and string[right] == " ":
            right -= 1
        while left <= right:
            char = string[left]
            if char != " ":
                chars.append(char)
            else:
                if chars[-1] != " ":
                    chars.append(" ")
            left += 1
        return chars

    def reverse(chars: List[str], left: int, right: int) -> None:
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

    chars = trim(s)
    length = len(chars)
    reverse(chars, 0, len(chars) - 1)
    i = j = 0
    while i < length:
        # 注意到达字符串末尾的情况
        while j < length and chars[j] != " ":
            j += 1
        reverse(chars, i, j - 1)
        j += 1
        i = j
    return "".join(chars)


if __name__ == "__main__":
    for func in reverse_words, reverse_words2:
        assert func("  hello world  ") == "world hello"
        assert func("the sky is blue") == "blue is sky the"
        assert func("a good   example") == "example good a"

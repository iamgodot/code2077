# 给你一个字符串 s ，逐个翻转字符串中的所有 单词 。


# 可以调用 API，也可以先全翻转再单个翻转，也可以用 deque. 复杂度都一样（对 Python 来说）
# 时间复杂度：O(n)
# 空间复杂度：O(n)
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


if __name__ == "__main__":
    s = "  Bob    Loves  Alice   "
    assert reverse_words(s) == "Alice Loves Bob"
    s = "the sky is blue"
    print(reverse_words(s))

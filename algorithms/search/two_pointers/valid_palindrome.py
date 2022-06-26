# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。


def valid_palindrome(s: str) -> bool:
    def is_palindrome(s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    i, j = 0, len(s) - 1
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
            continue
        return is_palindrome(s[i:j]) or is_palindrome(s[i + 1 : j + 1])

    return True


if __name__ == "__main__":
    assert valid_palindrome("aba") is True
    assert valid_palindrome("abca") is True
    assert valid_palindrome("abc") is False

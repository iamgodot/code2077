# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
# 说明：本题中，我们将空字符串定义为有效的回文串。


def is_valid_palindrome(s: str) -> bool:
    """
    注意字符串的大小写和字符类型判断。

    Time: O(n)
    Space: O(1)
    """
    i, j = 0, len(s) - 1
    while i < j:
        char_left, char_right = s[i].lower(), s[j].lower()
        if not char_left.isalnum():
            i += 1
            continue
        if not char_right.isalnum():
            j -= 1
            continue
        if char_left != char_right:
            return False
        else:
            i += 1
            j -= 1
    return True


# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。


def valid_palindrome(s: str) -> bool:
    """
    Time: O(n)
    Space: O(1)
    """

    def check_palindrome(left: int, right: int) -> bool:
        i, j = left, right
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
        return check_palindrome(i, j - 1) or check_palindrome(i + 1, j)

    return True


if __name__ == "__main__":
    assert is_valid_palindrome("A man, a plan, a canal: Panama") is True
    assert is_valid_palindrome("race a car") is False
    assert valid_palindrome("aba") is True
    assert valid_palindrome("abca") is True
    assert valid_palindrome("abc") is False

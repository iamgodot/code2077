# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

# 有效字符串需满足：

# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。


# 时间复杂度 O(n) 空间复杂度 O(n)
def is_valid(s: str) -> bool:
    """
    Stack: push '([{', pop when ')]}'
    Cases:
        1. Stack not empty: '('
        2. Type not match: '(]'
        3. Number not match: ']'
    """
    stack = []
    mappings = {"(": ")", "[": "]", "{": "}"}
    for char in s:
        if char in mappings.keys():
            stack.append(char)
            continue
        if not stack or mappings[stack.pop()] != char:
            return False

    return len(stack) == 0


if __name__ == "__main__":
    assert is_valid("(") is False
    assert is_valid("(]") is False
    assert is_valid("]") is False
    assert is_valid("()[]{}") is True
    assert is_valid("([{}])") is True

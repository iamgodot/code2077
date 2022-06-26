# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。


def is_valid(s: str) -> bool:
    """
    Time: O(n)
    Space: O(n)
    """
    mappings = {")": "(", "}": "{", "]": "["}
    stack = []

    for char in s:
        if char in "({[":
            stack.append(char)
        else:
            if not stack or stack.pop() != mappings[char]:
                return False

    return len(stack) == 0


if __name__ == "__main__":
    for string, validity in (
        ("()", True),
        ("(){}[]", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
    ):
        assert is_valid(string) == validity

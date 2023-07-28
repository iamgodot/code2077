# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。


def is_valid(s: str) -> bool:
    """
    Time: O(n)
    Space: O(n)
    """
    mappings = {")": "(", "}": "{", "]": "["}
    stack = []

    for char in s:
        if char in mappings.values():
            stack.append(char)
        else:
            if not stack or stack.pop() != mappings[char]:
                return False

    return len(stack) == 0


# 给定一个只包含三种字符的字符串：（ ，） 和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则：

# 任何左括号 ( 必须有相应的右括号 )。
# 任何右括号 ) 必须有相应的左括号 ( 。
# 左括号 ( 必须在对应的右括号之前 )。
# * 可以被视为单个右括号 ) ，或单个左括号 ( ，或一个空字符串。
# 一个空字符串也被视为有效字符串。


def check_valid_string(s: str) -> bool:
    """
    使用两个栈，分别保存左括号和星号的下标。

    Time: O(n)
    Space: O(n)
    """
    stack1, stack2 = [], []
    for i, char in enumerate(s):
        if char == "(":
            stack1.append(i)
        elif char == "*":
            stack2.append(i)
        else:
            if stack1:
                stack1.pop()
            elif stack2:
                stack2.pop()
            else:
                return False

    while stack1:
        # 注意星号的下标必须大于左括号才是有效的
        if not stack2 or stack2[-1] < stack1[-1]:
            return False
        stack1.pop()
        stack2.pop()

    return True


if __name__ == "__main__":
    for string, validity in (
        ("()", True),
        ("(){}[]", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
    ):
        assert is_valid(string) is validity
    for string, validity in (
        ("()", True),
        ("(*)", True),
        ("(*))", True),
    ):
        assert check_valid_string(string) is validity

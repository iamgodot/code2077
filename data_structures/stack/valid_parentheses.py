# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。


# 时间和空间复杂度都是 O(n)
def is_valid(s: str) -> bool:
    SYMBOL_MAPPINGS = {')': '(', '}': '{', ']': '['}
    stack = list()

    for char in s:
        if char in '({[':
            stack.append(char)
        else:
            if not stack or stack.pop() != SYMBOL_MAPPINGS[char]:
                return False

    return len(stack) == 0


if __name__ == '__main__':
    for s, validity in ('()', True), ('(){}[]',
                                      True), ('(]', False), ('([)]',
                                                             False), ('{[]}',
                                                                      True):
        assert is_valid(s) == validity

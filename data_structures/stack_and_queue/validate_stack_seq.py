# 给定 pushed 和 popped 两个序列，每个序列中的 值都不重复，只有当它们可能是在最初空栈上进行的推入 push 和弹出 pop 操作序列的结果时，返回 true；否则，返回 false 。


# 模拟栈的入栈和出栈操作，检查是否能满足结果
# 时间复杂度 O(n) 空间复杂度 O(n) 因为使用了辅助栈
def validate(pushed: list, popped: list) -> bool:
    stack = []
    index = 0
    for num in pushed:
        stack.append(num)
        while stack and stack[-1] == popped[index]:
            stack.pop()
            index += 1

    return stack == []


if __name__ == "__main__":
    assert validate([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]) is True
    assert validate([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]) is False

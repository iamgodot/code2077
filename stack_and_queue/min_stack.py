# 实现一个栈，这个栈的 push/pop/min 方法都可以达到 O(1) 的时间复杂度


class MinStack:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def empty(self) -> bool:
        return len(self.s1) == 0

    def push(self, val):
        self.s1.append(val)
        if not self.s2 or val <= self.s2[-1]:
            self.s2.append(val)

    def pop(self):
        if self.empty():
            return
        val = self.s1.pop()
        if self.s2 and val == self.s2[-1]:
            self.s2.pop()
        return val

    def min(self):
        if self.empty():
            return
        return self.s2[-1]


if __name__ == "__main__":
    min_stack = MinStack()
    assert min_stack.empty()
    assert min_stack.pop() is None
    assert min_stack.min() is None
    for i in [2, 1, 3]:
        min_stack.push(i)
    assert min_stack.min() == 1
    assert min_stack.pop() == 3
    assert min_stack.min() == 1
    assert min_stack.pop() == 1
    assert min_stack.min() == 2

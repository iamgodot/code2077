# Implement Stack using Queues
# https://leetcode.com/problems/implement-stack-using-queues/


class MyStack:
    def __init__(self):
        self.q1 = list()
        self.q2 = list()

    def push(self, x: int) -> None:
        self.q2.insert(0, x)

        while self.q1:
            self.q2.insert(0, self.q1.pop())
        self.q1, self.q2 = self.q2, self.q1

    def empty(self) -> bool:
        return not self.q1

    def pop(self) -> int:
        if self.empty():
            return None

        return self.q1.pop()

    def top(self) -> int:
        if self.empty():
            return None

        return self.q1[-1]


# 也可以用一个队列实现，更好理解，复杂度同上
class MyStackV2:
    def __init__(self):
        self.q = list()

    def push(self, x: int) -> None:
        self.q.insert(0, x)

        for _ in range(len(self.q) - 1):
            self.q.insert(0, self.q.pop())

    def empty(self) -> bool:
        return not self.q

    def pop(self) -> int:
        if self.empty():
            return None

        return self.q.pop()

    def top(self) -> int:
        if self.empty():
            return None

        return self.q[-1]


if __name__ == "__main__":
    for stack_cls in [MyStack, MyStackV2]:
        stack = stack_cls()
        stack.push(1)
        stack.push(2)
        assert stack.top() == 2
        assert stack.pop() == 2
        assert not stack.empty()

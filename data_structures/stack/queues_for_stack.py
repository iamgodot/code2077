# 请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（push、top、pop 和 empty）
# 进阶：你能否实现每种操作的均摊时间复杂度为 O(1) 的栈？
# 换句话说，执行 n 个操作的总时间复杂度 O(n) ，尽管其中某个操作可能需要比其他操作更长的时间。你可以使用两个以上的队列。

# push 操作耗时 O(n)，其他都是 O(1)
# 感觉做不到所有操作都保证 O(1)


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
        '''相当于调用了队列的 peek 方法'''
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


if __name__ == '__main__':
    for stack_cls in [MyStack, MyStackV2]:
        stack = stack_cls()
        stack.push(1)
        stack.push(2)
        assert stack.top() == 2
        assert stack.pop() == 2
        assert not stack.empty()

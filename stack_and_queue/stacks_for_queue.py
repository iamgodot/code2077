# 请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）
# 进阶：你能否实现每个操作均摊时间复杂度为 O(1) 的队列？
# 换句话说，执行 n 个操作的总时间复杂度为 O(n) ，即使其中一个操作可能花费较长时间。

# 设置输入栈和输出栈，可以保证 push 永远耗时 O(1)，而 pop 操作仅在输出栈需要填充时为 O(n)
# 综合下来也是 O(1)，满足进阶的条件。
# 如果尝试在 push 或者 pop 的时候先全部出栈再填回的方式是无法满足进阶要求的
# 即 push/pop 中一定有一个耗时会达到 O(n)


class MyQueue:
    def __init__(self):
        self.stack_in = list()
        self.stack_out = list()

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if self.empty():
            return None

        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        return self.stack_out.pop()

    def peek(self) -> int:
        '''Use pop() to implement instead of code copying'''
        val = self.pop()

        if val:
            self.stack_out.append(val)  # Must not use push() here

        return val

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out


if __name__ == '__main__':
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    assert queue.peek() == 1
    assert queue.pop() == 1
    assert not queue.empty()

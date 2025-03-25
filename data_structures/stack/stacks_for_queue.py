# Implement Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/description/


class MyQueue:
    """
    Use two stacks, remember to name them properly.
    Also clarify if the queue could be empty when popping.

    Time: O(1), amortized for popping
    Space: O(n)
    """

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

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
        """Use pop() to implement instead of code copying"""
        val = self.pop()

        if val:
            self.stack_out.append(val)  # Must not use push() here

        return val

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out


if __name__ == "__main__":
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    assert queue.peek() == 1
    assert queue.pop() == 1
    assert not queue.empty()

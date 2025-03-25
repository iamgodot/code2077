# Min Stack
# https://leetcode.com/problems/min-stack/description/


class MinStack:
    """
    Use a subsidiary stack to keep track of the minimum value.

    Time: O(1)
    Space: O(n)
    """

    def __init__(self):
        self.stack = []
        self.stack_min = []

    def push(self, val):
        self.stack.append(val)
        if not self.stack_min or val <= self.stack_min[-1]:
            self.stack_min.append(val)

    def pop(self):
        val = self.stack.pop()
        if self.stack_min and val == self.stack_min[-1]:
            self.stack_min.pop()
        return val

    def min(self):
        return self.stack_min[-1]


class MinStack2:
    """
    Use a variable to keep track of the minimum value, and only store diffs in the stack.

    Time: O(1)
    Space: O(1)
    """

    def __init__(self):
        self.s = []
        self.min_val = 0

    def push(self, val: int) -> None:
        # NOTE: here don't check with min_val
        if not self.s:
            self.s.append(0)
            self.min_val = val
        else:
            self.s.append(val - self.min_val)
            if val < self.min_val:
                self.min_val = val

    def pop(self) -> int:
        if self.s[-1] < 0:
            res = self.min_val
            self.min_val -= self.s[-1]
            return res
        return self.s.pop() + self.min_val

    def top(self) -> int:
        if self.s[-1] < 0:
            return self.min_val
        else:
            return self.min_val + self.s[-1]

    def min(self) -> int:
        return self.min_val


if __name__ == "__main__":
    for cls in MinStack, MinStack2:
        min_stack = cls()
        for i in [2, 1, 3]:
            min_stack.push(i)
        assert min_stack.min() == 1
        assert min_stack.pop() == 3
        assert min_stack.min() == 1
        assert min_stack.pop() == 1
        assert min_stack.min() == 2

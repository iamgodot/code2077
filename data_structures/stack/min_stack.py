# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

# push(x) —— 将元素 x 推入栈中。
# pop() —— 删除栈顶的元素。
# top() —— 获取栈顶元素。
# getMin() —— 检索栈中的最小元素。

# pop、top 和 getMin 操作总是在 非空栈 上调用。


# 1. 使用辅助栈保存当前最小值
# 空间复杂度 O(n)
class MinStack:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, val):
        self.s1.append(val)
        if not self.s2 or val <= self.s2[-1]:
            self.s2.append(val)

    def pop(self):
        val = self.s1.pop()
        if self.s2 and val == self.s2[-1]:
            self.s2.pop()
        return val

    def min(self):
        return self.s2[-1]


# 2. 使用变量保存当前最小值，栈中保存元素与最小值的差值 diff
# 空间复杂度 O(1)
class MinStack2:
    def __init__(self):
        self.s = []
        self.min_val = 0

    def push(self, val: int) -> None:
        # 注意这里不要根据 min_val is None 来做判断条件
        # 因为过程中 min_val 可能会被置为非空值，即使栈中已经没有元素
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

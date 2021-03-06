# 设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”。

# 循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存储新的值。

# 你的实现应该支持如下操作：

# MyCircularQueue(k): 构造器，设置队列长度为 k 。
# Front: 从队首获取元素。如果队列为空，返回 -1 。
# Rear: 获取队尾元素。如果队列为空，返回 -1 。
# enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
# deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
# isEmpty(): 检查循环队列是否为空。
# isFull(): 检查循环队列是否已满。


class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [0] * k
        self.head_index = 0
        self.size = 0
        self.capacity = k

    def get_insert_index(self):
        return (self.head_index + self.size) % self.capacity

    def enQueue(self, value: int) -> bool:
        if self.size == self.capacity:
            return False
        self.queue[self.get_insert_index()] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        self.queue[self.head_index] = 0
        self.head_index = (self.head_index + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.queue[self.head_index]

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.queue[self.get_insert_index() - 1]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


if __name__ == "__main__":
    q = MyCircularQueue(3)
    for i in range(1, 4):
        assert q.enQueue(i) is True
    assert q.enQueue(4) is False
    assert q.Rear() == 3
    assert q.isFull() is True
    assert q.deQueue() is True
    assert q.enQueue(4) is True
    assert q.Rear() == 4

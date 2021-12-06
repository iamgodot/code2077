# 不使用任何内建的哈希表库设计一个哈希集合（HashSet）。
# 实现 MyHashSet 类：
# void add(key) 向哈希集合中插入值 key 。
# bool contains(key) 返回哈希集合中是否存在这个值 key 。
# void remove(key) 将给定值 key 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。


# 时间复杂度 O(n/b)，n 为元素总数，b 为 bucket 总数
# 空间复杂度 O(n + b)
class MyHashSet:
    def __init__(self):
        self.size = 10000
        self.array = [[] for _ in range(self.size)]

    def _find_bucket(self, key: int) -> list:
        return self.array[key % self.size]

    def add(self, key: int) -> None:
        if not self.contains(key):
            self._find_bucket(key).append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self._find_bucket(key).remove(key)

    def contains(self, key: int) -> bool:
        return key in self._find_bucket(key)


if __name__ == "__main__":
    hashset = MyHashSet()
    hashset.add(1)
    hashset.add(2)
    assert hashset.contains(1) is True
    assert hashset.contains(3) is False
    hashset.add(2)
    assert hashset.contains(2) is True
    hashset.remove(2)
    assert hashset.contains(2) is False

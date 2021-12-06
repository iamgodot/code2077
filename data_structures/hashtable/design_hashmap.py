# 不使用任何内建的哈希表库设计一个哈希映射（HashMap）。

# 实现 MyHashMap 类：

# MyHashMap() 用空映射初始化对象
# void put(int key, int value) 向 HashMap 插入一个键值对 (key, value) 。如果 key 已经存在于映射中，则更新其对应的值 value 。
# int get(int key) 返回特定的 key 所映射的 value ；如果映射中不包含 key 的映射，返回 -1 。
# void remove(key) 如果映射中存在 key 的映射，则移除 key 和它所对应的 value 。


# 时间复杂度 O(n/b)，n 为元素总数，b 为 bucket 总数
# 空间复杂度 O(n + b)
class MyHashMap:
    def __init__(self):
        self.size = 10000
        self.array = [[] for _ in range(self.size)]

    def _find_bucket(self, key: int) -> list:
        return self.array[key % self.size]

    def _find_item(self, key: int) -> list:
        bucket = self._find_bucket(key)
        for item in bucket:
            if item[0] == key:
                return item

        return []

    def put(self, key: int, value: int) -> None:
        bucket = self._find_bucket(key)
        if item := self._find_item(key):
            item[1] = value
        else:
            bucket.append([key, value])

    def get(self, key: int) -> int:
        if item := self._find_item(key):
            return item[1]

        return -1

    def remove(self, key: int) -> None:
        bucket = self._find_bucket(key)
        if item := self._find_item(key):
            bucket.remove(item)


if __name__ == "__main__":
    hashmap = MyHashMap()
    hashmap.put(1, 1)
    hashmap.put(2, 2)
    assert hashmap.get(1) == 1
    assert hashmap.get(3) == -1
    hashmap.put(2, 1)
    assert hashmap.get(2) == 1
    hashmap.remove(2)
    assert hashmap.get(2) == -1

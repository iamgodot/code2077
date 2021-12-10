# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
# 你可以按 任何顺序 返回答案。


# 时间复杂度：O(C(n, k)*k)
# 空间复杂度：O(n) 其中递归栈空间为 O(k)
def combine(n: int, k: int) -> list:
    def bt(n, k, start) -> None:
        length = len(path)
        if length == k:
            res.append(path[:])
            return
        for i in range(start, n - (k - length) + 1):
            path.append(i + 1)
            bt(n, k, i + 1)
            path.pop()

    res, path = [], []
    bt(n, k, 0)
    return res


if __name__ == "__main__":
    assert combine(4, 2) == sorted(
        [
            [2, 4],
            [3, 4],
            [2, 3],
            [1, 2],
            [1, 3],
            [1, 4],
        ]
    )
    assert combine(1, 1) == [[1]]

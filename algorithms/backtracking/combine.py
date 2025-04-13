# Combinations
# https://leetcode.com/problems/combinations/description/


def combine(n: int, k: int) -> list:
    """
    Time: O(C(n, k)*k)
    Space: O(n) and O(k) for the recursive stack
    """
    res, path = [], []

    def bt(index) -> None:
        if len(path) == k:
            res.append(path.copy())
            return
        for index in range(index, n):
            path.append(index + 1)
            bt(index + 1)
            path.pop()

    bt(0)
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

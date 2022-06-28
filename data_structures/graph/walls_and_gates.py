# 你被给定一个 m × n 的二维网格，网格中有以下三种可能的初始化值：

# -1 表示墙或是障碍物
# 0 表示一扇门
# INF 无限表示一个空的房间。然后，我们用 2^31 - 1 = 2147483647 代表 INF。你可以认为通往门的距离总是小于 2147483647 的。
# 你要给每个空房间位上填上该房间到 最近 门的距离，如果无法到达门，则填 INF 即可。


from typing import List


def walls_and_gates(rooms: List[List[int]]) -> None:
    if not rooms or not rooms[0]:
        return
    m, n = len(rooms), len(rooms[0])
    from collections import deque

    dq = deque([])
    for i in range(m):
        for j in range(n):
            if rooms[i][j] == 0:
                dq.append((i, j, 0))

    while dq:
        i, j, distance = dq.pop()
        for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
            if 0 <= x < m and 0 <= y < n and rooms[x][y] == float("inf"):
                dq.appendleft((x, y, distance + 1))
                rooms[x][y] = distance + 1


if __name__ == "__main__":
    inf = float("inf")
    grid = [
        [inf, -1, 0, inf],
        [inf, inf, inf, -1],
        [inf, -1, inf, -1],
        [0, -1, inf, inf],
    ]
    walls_and_gates(grid)
    assert grid == [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]

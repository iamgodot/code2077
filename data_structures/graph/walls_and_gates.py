# Walls and Gates
# https://leetcode.com/problems/walls-and-gates/description/


def walls_and_gates(rooms: list[list[int]]) -> None:
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

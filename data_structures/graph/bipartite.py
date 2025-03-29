# Is Graph Bipartite?
# https://leetcode.com/problems/is-graph-bipartite/description/


def is_bipartite(graph: list[list[int]]) -> bool:
    """
    Time: O(n+m) 其中 nn 和 mm 分别是无向图中的点数和边数
    Space: O(n)
    """
    n = len(graph)
    from collections import deque

    visited = [0] * n

    # 可能不是连通图，所以要 for loop
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            dq = deque([i])
            while dq:
                node = dq.pop()
                value = visited[node]
                for nb in graph[node]:
                    if visited[nb] == 0:
                        dq.appendleft(nb)
                        visited[nb] = 2 if value == 1 else 1
                    elif visited[nb] == value:
                        return False

    return True


if __name__ == "__main__":
    assert is_bipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]) is False
    assert is_bipartite([[1, 3], [0, 2], [1, 3], [0, 2]]) is True

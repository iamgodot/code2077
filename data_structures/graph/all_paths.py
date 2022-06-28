# 给你一个有 n 个节点的 有向无环图（DAG），请你找出所有从节点 0 到节点 n-1 的路径并输出（不要求按特定顺序）
#  graph[i] 是一个从节点 i 可以访问的所有节点的列表（即从节点 i 到节点 graph[i][j]存在一条有向边）。

from typing import List


def all_paths(graph: List[List[int]]) -> List[List[int]]:
    def dfs(index):
        path.append(index)
        if len(graph) == index + 1:
            res.append(path[:])
        for nb in graph[index]:
            dfs(nb)
        path.pop()

    res, path = [], []
    dfs(0)
    return res


if __name__ == "__main__":
    assert all_paths([[1, 2], [3], [3], []]) == [[0, 1, 3], [0, 2, 3]]

# 图

## 概念

- 顶点 Vertex
- 边 Edge

1. 有向图 vs 无向图

顶点的度：边数，对于有向图来说是入度 + 出度。

2. 环形图 vs 无环图

一个图中的路径包括环和简单路径。

有向无环图 DAG(Directed Acyclic Graph)
因为有向无环图拥有为独特的拓扑结构，经常被用于处理动态规划、导航中寻求最短路径、数据压缩等多种算法场景。

3. 连通图 vs 非连通图

4. 带权图

每条边都被赋予一个权值。

带权的连通无向图称为网络。

## 存储结构

- 顺序
  - 邻接矩阵：查询快 O(1)，耗费空间大。
  - 边集数组：按边存储，查询慢，适合对边依次进行处理的运算。
- 链式
  - 邻接表：哈希表保存顶点，每个顶点对象里再用哈希表保存到另一个顶点的边。

## 遍历

DFS 和 BFS 的复杂度都和图的大小线性相关：

- Time: O(n)
- Space: O(n)

DFS 注意 Stackoverflow，BFS 注意邻节点数量带来的空间占用

### DFS

图的节点结构和树很像，但是图可能包含环（除非是 DAG），所以要记录遍历过的节点：

```python
def dfs(graph, node, visited, path):
    if visited[node]:
        return
    visited[node] = True
    # 在路径中添加 node
    path.append(node)
    # 满足特定条件之后在 res 中记录 path
    if ...:
        res.append(path[:])
    for neighbor in neighbors:
        dfs(graph, neighbor, visited, path)
    # 从路径中删除 node
    # 注意不是在上面每次递归 dfs 之后删除
    path.pop()
```

### BFS

可以分为两种类型，非层序和层序遍历，看是否需要计算层数。

```python
def bfs(node, visited):
    from collections import deque
    dq = deque([node])
    visited[node] = True
    while dq:
        item = dq.pop()
        for nb in item.neighbors:
            if not visited[nb]:
                dq.appendleft(nb)
                visited[nb] = True
```

```python
def bfs(node, visited):
    from collections import deque
    dq = deque([node])
    visited[node] = True
    step = 0
    while dq:
        for i in range(len(dq)):
            item = dq.pop()
            for nb in item.neighbors:
                if not visited[nb]:
                    dq.appendleft(nb)
                    visited[nb] = True
        step += 1
```

## 拓扑排序

## 题目

- 遍历
  - 树的路径类题目 -> dfs
  - [岛屿数量](num_island.py)
  - [最大岛屿面积](max_area.py)
  - [岛屿周长](perimeter.py)
  - [最大人工岛](largest_island.py)
  - [被围绕的区域](surrounded_regions.py)
  - [克隆图](clone_graph.py)
  - [所有可能的路径](all_paths.py)
  - BFS
    - [墙与门](walls_and_gates.py)
    - [腐烂的橘子](rotting_oranges.py)
    - [判断二分图](bipartite.py)
- 拓扑排序
  - [课程表](courses.py)

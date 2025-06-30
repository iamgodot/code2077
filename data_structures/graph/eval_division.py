# Evaluate Division
# https://leetcode.com/problems/evaluate-division/


def calcEquation(
    equations: list[list[str]], values: list[float], queries: list[list[str]]
) -> list[float]:
    """Can also use union-find.

    https://leetcode.cn/problems/evaluate-division/solutions/3073580/wei-zhuang-cheng-zhong-deng-ti-de-kun-na-j9sm/
    """
    # create the graph
    from collections import defaultdict

    graph = defaultdict(dict)
    for (s, e), v in zip(equations, values):
        graph[s][e] = v
        graph[e][s] = 1 / v

    # dfs
    def dfs(cur, tgt, accum, visited):
        if cur == tgt:
            return accum
        if cur in visited:
            return -1.0
        visited.add(cur)
        for nbr, val in graph[cur].items():
            tmp = dfs(nbr, tgt, accum * val, visited)
            if tmp != -1.0:
                return tmp
        return -1.0

    # solving the queries
    ans = []
    for s, e in queries:
        if s not in graph or e not in graph:
            ans.append(-1.0)
        else:
            ans.append(dfs(s, e, 1.0, set()))
    return ans

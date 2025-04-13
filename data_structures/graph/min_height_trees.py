# Minimum Height Trees
# https://leetcode.com/problems/minimum-height-trees/description/


def findMinHeightTrees(n: int, edges: list[list[int]]) -> list[int]:
    """
    Topological sort.

    Time: O(n) where n is the number of nodes
    Space: O(n)
    """
    if n <= 2:
        return [i for i in range(n)]
    from collections import defaultdict

    adj = defaultdict(set)
    for n1, n2 in edges:
        adj[n1].add(n2)
        adj[n2].add(n1)
    leaves = []
    for node in adj:
        if len(adj[node]) == 1:
            leaves.append(node)
    size = len(adj)
    while size > 2:
        size -= len(leaves)
        leaves_new = []
        for leaf in leaves:
            parent = adj[leaf].pop()
            adj[parent].remove(leaf)
            if len(adj[parent]) == 1:
                leaves_new.append(parent)
        leaves = leaves_new
    return leaves

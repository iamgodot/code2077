# 给你无向 连通 图中一个节点的引用，请你返回该图的 深拷贝（克隆）。


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone(node: Node) -> Node:
    """
    Time: O(n)
    Space: O(n)
    """

    def dfs(node) -> Node:
        if not node:
            return None
        if node in hashtable:
            return hashtable[node]
        cloned = Node(node.val, [])
        hashtable[node] = cloned
        for nb in node.neighbors:
            cloned.neighbors.append(dfs(nb))
        return cloned

    hashtable = {}
    return dfs(node)


def clone2(node: Node) -> Node:
    """
    Time: O(n)
    Space: O(n)
    """

    def bfs(node) -> Node:
        if not node:
            return None
        from collections import deque

        dq = deque([node])
        cloned = Node(node.val, [])
        hashtable = {node: cloned}
        while dq:
            item = dq.pop()
            for nb in item.neighbors:
                if nb not in hashtable:
                    dq.appendleft(nb)
                    hashtable[nb] = Node(node.val, [])
                hashtable[item].neighbors.append(hashtable[nb])
        return

    return bfs(node)

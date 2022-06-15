# DFS
# - 前序遍历（递归法、迭代法）：中左右，从上到下，求深度，真正体现回溯
# - 中序遍历（递归法、迭代法）：左中右，体现了 BST 的排序特点
# - 后序遍历（递归法、迭代法）：左右中，自底向上，求高度
# BFS
# - 层序遍历（迭代法、队列）

# 对于深度优先来说，时间复杂度为 O(n)，而空间复杂度为 O(h)，树的高度可能为 O(n) 也可能为 O(logn)
# 对于广度优先来说，时间复杂度为 O(n)，递归实现的空间复杂度为 O(h)，而非递归版本空间复杂度为 O(n)

from typing import List, Optional

from data_structures.tree import TreeNode


def preorder(root: TreeNode, values: list):
    if not root:
        return
    values.append(root.val)
    preorder(root.left, values)
    preorder(root.right, values)


def inorder(root: TreeNode, values: list):
    if not root:
        return
    inorder(root.left, values)
    values.append(root.val)
    inorder(root.right, values)


def postorder(root: TreeNode, values: list):
    if not root:
        return
    postorder(root.left, values)
    postorder(root.right, values)
    values.append(root.val)


def preorder_it(root: TreeNode):
    stack, res = [], []
    cur = root
    while cur or stack:
        if cur:
            res.append(cur.val)
            stack.append(cur.right)
            cur = cur.left
        else:
            cur = stack.pop()

    return res


def inorder_it(root: TreeNode):
    stack, res = [], []
    cur = root
    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right

    return res


def postorder_it(root: TreeNode):
    stack, res = [], []
    cur = root
    while cur or stack:
        if cur:
            res.append(cur.val)
            stack.append(cur.left)
            cur = cur.right
        else:
            cur = stack.pop()

    return res[::-1]


def levelorder(root: TreeNode):
    res = []
    if not root:
        return res

    from collections import deque

    dq = deque([root])
    while dq:
        size = len(dq)
        level = []
        for _ in range(size):
            node = dq.pop()
            level.append(node.val)
            if node.left:
                dq.appendleft(node.left)
            if node.right:
                dq.appendleft(node.right)
        res.append(level)

    return res


def levelorder_rec(root):
    res = []

    def _order(root, level):
        if not root:
            return
        if len(res) == level:
            res.append([])
        res[level].append(root.val)
        _order(root.left, level + 1)
        _order(root.right, level + 1)

    _order(root, 0)
    return res


# 给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。


def zigzag_levelorder(root: TreeNode) -> List[List[int]]:
    res = []
    if not root:
        return res
    from collections import deque

    dq = deque([root])
    while dq:
        level = []
        for _ in range(len(dq)):
            node = dq.pop()
            if len(res) % 2 == 0:
                level.append(node.val)
            else:
                level.insert(0, node.val)
            if node.left:
                dq.appendleft(node.left)
            if node.right:
                dq.appendleft(node.right)
        res.append(level)
    return res


# 给你一个二叉树的根结点，返回其结点按 垂直方向（从上到下，逐列）遍历的结果。
# 如果两个结点在同一行和列，那么顺序则为 从左到右。


def vertical_order(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    res = []
    from collections import defaultdict, deque

    dq = deque([[root, 0]])  # [node, key]
    key_to_vals = defaultdict(list)
    while dq:
        node, key = dq.pop()
        key_to_vals[key].append(node.val)
        if node.left:
            dq.appendleft([node.left, key - 1])
        if node.right:
            dq.appendleft([node.right, key + 1])
    for k in sorted(key_to_vals):
        res.append(key_to_vals[k])
    return res


if __name__ == "__main__":
    tree = TreeNode(
        val=1,
        left=TreeNode(val=2, left=TreeNode(4), right=TreeNode(5)),
        right=TreeNode(val=3, left=TreeNode(6), right=TreeNode(7)),
    )
    # 1
    # | \
    # 2  3
    # |\ |\
    # 4 56 7

    for traversal, nums in [
        (preorder, [1, 2, 4, 5, 3, 6, 7]),
        (inorder, [4, 2, 5, 1, 6, 3, 7]),
        (postorder, [4, 5, 2, 6, 7, 3, 1]),
    ]:
        res = []
        traversal(tree, res)
        assert res == nums

    for traversal, nums in [
        (preorder_it, [1, 2, 4, 5, 3, 6, 7]),
        (inorder_it, [4, 2, 5, 1, 6, 3, 7]),
        (postorder_it, [4, 5, 2, 6, 7, 3, 1]),
    ]:
        assert traversal(tree) == nums

    assert levelorder(tree) == [[1], [2, 3], [4, 5, 6, 7]]
    assert levelorder_rec(tree) == [[1], [2, 3], [4, 5, 6, 7]]
    assert zigzag_levelorder(tree) == [[1], [3, 2], [4, 5, 6, 7]]
    assert vertical_order(tree) == [[4], [2], [1, 5, 6], [3], [7]]

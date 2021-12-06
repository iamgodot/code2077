# 二叉树的遍历主要分为两种：
# 深度优先：前序/中序/后序
# 广度优先：层序
# 对于深度优先来说，时间复杂度为 O(n)，而空间复杂度为 O(h)，树的高度可能为 O(n) 也可能为 O(logn)
# 对于广度优先来说，时间复杂度为 O(n)，递归实现的空间复杂度为 O(h)，而非递归版本空间复杂度为 O(n)
# 因为非递归版本使用的队列会保存每一层的元素，而这里的元素数量也是指数增长的
from tree import TreeNode


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


if __name__ == "__main__":
    root = TreeNode(
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
        traversal(root, res)
        assert res == nums

    for traversal, nums in [
        (preorder_it, [1, 2, 4, 5, 3, 6, 7]),
        (inorder_it, [4, 2, 5, 1, 6, 3, 7]),
        (postorder_it, [4, 5, 2, 6, 7, 3, 1]),
    ]:
        assert traversal(root) == nums

    assert levelorder(root) == [[1], [2, 3], [4, 5, 6, 7]]
    assert levelorder_rec(root) == [[1], [2, 3], [4, 5, 6, 7]]

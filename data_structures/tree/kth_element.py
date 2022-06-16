# 给定一棵二叉搜索树，请找出其中第 k 大的节点的值。

from data_structures.tree import TreeNode


# 时间复杂度 O(n) 当树退化为链表时（全部为右子节点），无论 k 的值大小，递归深度都为 N ，占用 O(n) 时间
# 空间复杂度 O(n) 当树退化为链表时（全部为右子节点），系统使用 O(n) 大小的栈空间
def kth_largest(root: TreeNode, k: int) -> int:
    def traversal(root) -> None:
        nonlocal res, k
        if not root:
            return
        traversal(root.right)
        k -= 1
        if k == 0:
            res = root.val
            return
        traversal(root.left)

    res = None
    traversal(root)
    return res


def kth_largest_it(root, k) -> int:
    cur, stack = root, []
    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.right
        else:
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.left


# 给定一棵二叉搜索树，请找出其中第 k 大的节点的值。


def kth_smallest(root: TreeNode, k: int) -> int:
    def traversal(node: TreeNode) -> None:
        if not node:
            return
        traversal(node.left)
        nonlocal k, res
        k -= 1
        if k == 0:
            res = node.val
            return
        traversal(node.right)

    res = None
    traversal(root)
    return res


if __name__ == "__main__":
    tree = TreeNode(3, left=TreeNode(1, right=TreeNode(2)), right=TreeNode(4))
    assert kth_largest(tree, 2) == 3
    assert kth_smallest(tree, 2) == 2

# 给定一棵二叉搜索树，请找出其中第 k 大的节点的值。

from data_structures.tree import TreeNode


# 时间复杂度 O(n) 当树退化为链表时（全部为右子节点），无论 k 的值大小，递归深度都为 N ，占用 O(n) 时间
# 空间复杂度 O(n) 当树退化为链表时（全部为右子节点），系统使用 O(n) 大小的栈空间
def kth_largest(root: TreeNode, k: int) -> int:
    def traversal(root):
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


if __name__ == "__main__":
    root = TreeNode(3, left=TreeNode(1, right=TreeNode(2)), right=TreeNode(4))
    assert kth_largest(root, 1) == 4

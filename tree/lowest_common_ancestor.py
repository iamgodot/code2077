# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

from tree import TreeNode


# 需要自底向上回溯，因此通过递归调用的时候获取返回值，再对其进行判断
# 时间复杂度 O(n)
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root or root.val == p.val or root.val == q.val:
        return root

    ancestor_left = lowest_common_ancestor(root.left, p, q)
    ancestor_right = lowest_common_ancestor(root.right, p, q)

    if ancestor_left and ancestor_right:
        return root
    elif ancestor_left:
        return ancestor_left
    elif ancestor_right:
        return ancestor_right

    return None


if __name__ == "__main__":
    root = TreeNode(
        val=3,
        left=TreeNode(
            val=5,
            left=TreeNode(6),
            right=TreeNode(2, left=TreeNode(7), right=TreeNode(4)),
        ),
        right=TreeNode(val=1, left=TreeNode(val=0), right=TreeNode(8)),
    )
    node = lowest_common_ancestor(root, TreeNode(5), TreeNode(1))
    print(node.val)

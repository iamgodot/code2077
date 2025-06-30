# Binary Tree Paths
# https://leetcode.com/problems/binary-tree-paths/description/

from data_structures.tree import TreeNode


def binary_tree_path(root: TreeNode) -> list[str]:
    """
    Time: O(n^2)
    Space: O(n^2)
    """

    def dfs(node) -> None:
        if not node:
            return
        path.append(str(node.val))  # 注意要转换为字符串
        if not node.left and not node.right:
            res.append("->".join(path))
        dfs(node.left)
        dfs(node.right)
        path.pop()

    path, res = [], []
    dfs(root)
    return res

# 给定一个二叉树，判断它是否是高度平衡的二叉树。
# 本题中，一棵高度平衡二叉树定义为：
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。

from data_structures.tree import TreeNode


# 后序遍历
def is_balanced(root: TreeNode) -> bool:
    def get_depth(root: TreeNode) -> int:
        if not root:
            return 0
        depth_left = get_depth(root.left)
        if depth_left == -1:
            return -1
        depth_right = get_depth(root.right)
        if depth_right == -1:
            return -1
        if abs(depth_left - depth_right) > 1:
            return -1
        return max(depth_left, depth_right) + 1

    return get_depth(root) != -1


if __name__ == "__main__":
    # 3
    # |\
    # 9 20
    #   |\
    #  15 7
    root = TreeNode(
        val=3,
        left=TreeNode(val=9),
        right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(7)),
    )
    assert is_balanced(root) is True
    # 1
    # |\
    # 2 2
    # |\
    # 3 3
    # |\
    # 4 4
    root = TreeNode(
        val=1,
        left=TreeNode(
            val=2,
            left=TreeNode(val=3, left=TreeNode(val=4), right=TreeNode(val=4)),
            right=TreeNode(val=3),
        ),
        right=TreeNode(val=2),
    )
    assert is_balanced(root) is False

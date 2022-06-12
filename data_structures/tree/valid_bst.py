# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

from data_structures.tree import TreeNode


# 因为要判断 BST，所以要利用其特性也就应该做中序遍历
# 1. 直接中序遍历出结果数组，然后顺序判断，时间和空间复杂度都为 O(n)
# 2. 递归实现中序遍历，最坏情况下时间和空间复杂度也都为 O(n)
def is_valid_bst(root: TreeNode) -> bool:
    def is_valid(node: TreeNode) -> bool:
        if not node:
            return True
        nonlocal pre
        if not is_valid(node.left):
            return False
        if node.val <= pre:
            return False
        pre = node.val
        return is_valid(node.right)

    pre = -float("inf")
    return is_valid(root)

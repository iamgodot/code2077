# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

from data_structures.tree import TreeNode


# 因为要判断 BST，所以要利用其特性也就应该做中序遍历
# 1. 直接中序遍历出结果数组，然后顺序判断，时间和空间复杂度都为 O(n)
# 2. 递归实现中序遍历，时间复杂度 O(n) 空间复杂度 O(logn)
def is_valid_bst(self, root: TreeNode) -> bool:
    def is_valid(node: TreeNode) -> bool:
        nonlocal val
        if not node:
            return True
        left = is_valid(node.left)
        # 注意 val 可能为 0 所以要显式判断是否为 None
        # 另外等于的情况也要排除
        if val is not None and val >= node.val:
            return False
        val = node.val
        right = is_valid(node.right)
        return left and right

    val = None
    return is_valid(root)

# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。


from data_structures.tree import TreeNode


# 在求最大深度的过程中更新 max_ 的值
# 时间复杂度 O(n) 空间复杂度 O(h)
def diameter_of_binary_tree(root: TreeNode) -> int:
    def get_depth(node) -> int:
        nonlocal max_
        if not node:
            return 0
        left = get_depth(node.left)
        right = get_depth(node.right)
        max_ = max(max_, left + right)
        return max(left, right) + 1

    max_ = -float("inf")
    get_depth(root)
    return max_

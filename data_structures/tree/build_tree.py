# 给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。

from typing import List

from data_structures.tree import TreeNode


# 1. preorder 确认根节点和左子节点 -> 2. inorder 确认根节点左右的子树长度 -> 3. preorder 确认两个子树的根节点位置，其实主要是右子节点的位置
# 时间复杂度 O(n)
# 空间复杂度 O(n) 其中哈希表占用 O(n) 递归占用 O(h)
def build_tree(preorder: List[int], inorder: List[int]) -> TreeNode:
    def _build(index, left, right) -> TreeNode:
        if left > right:
            return None
        val = preorder[index]
        root = TreeNode(val)
        i = hashtable[val]
        root.left = _build(index + 1, left, i - 1)
        # 左子节点的位置 index+1 加上左子树的长度 i-1-left+1
        root.right = _build(index + 1 + i - left, i + 1, right)
        return root

    hashtable = {val: pos for pos, val in enumerate(inorder)}
    return _build(0, 0, len(inorder) - 1)


# 给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，请你构造并返回这颗 二叉树 。


# 时间复杂度 O(n)
# 空间复杂度 O(n) 其中哈希表占用 O(n) 递归占用 O(h)
def build_tree(inorder: List[int], postorder: List[int]) -> TreeNode:
    def build(index, left, right) -> TreeNode:
        if left > right:
            return None
        val = postorder[index]
        root = TreeNode(val)
        i = hashtable[val]
        root.left = build(index - 1 - (right - i), left, i - 1)
        root.right = build(index - 1, i + 1, right)
        return root

    hashtable = {val: pos for pos, val in enumerate(inorder)}
    return build(len(postorder) - 1, 0, len(inorder) - 1)


# 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。
# 高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。


def sorted_array_to_bst(nums: List[int]) -> TreeNode:
    def build(left, right) -> TreeNode:
        if left > right:
            return None

        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        node.left = build(left, mid - 1)
        node.right = build(mid + 1, right)
        return node

    return build(0, len(nums) - 1)

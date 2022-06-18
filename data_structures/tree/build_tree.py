# 给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。

from typing import List

from data_structures.tree import TreeNode


# 1. preorder 确认根节点和左子节点 -> 2. inorder 确认根节点左右的子树长度 -> 3. preorder 确认两个子树的根节点位置，其实主要是右子节点的位置
# 时间复杂度 O(n)
# 空间复杂度 O(h)
def build_tree(preorder: List[int], inorder: List[int]) -> TreeNode:
    def _build(index, left, right) -> TreeNode:
        if left > right:
            return None
        val = preorder[index]
        root = TreeNode(val)
        i = inorder.index(val)
        root.left = _build(index + 1, left, i - 1)
        # 左子节点的位置 index+1 加上左子树的长度 i-1-left+1
        root.right = _build(index + 1 + i - left, i + 1, right)
        return root

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
        i = inorder.index(val)
        root.left = build(index - 1 - (right - i), left, i - 1)
        root.right = build(index - 1, i + 1, right)
        return root

    return build(len(postorder) - 1, 0, len(inorder) - 1)


# 给定两个整数数组，preorder 和 postorder ，其中 preorder 是一个具有 无重复 值的二叉树的前序遍历，postorder 是同一棵树的后序遍历，重构并返回二叉树。
# 如果存在多个答案，您可以返回其中 任何 一个。


def build_tree(preorder: List[int], postorder: List[int]) -> TreeNode:
    """
    前序遍历的第一个元素为 root，第二个元素为 root.left，
    根据 left 找出其在后序遍历中的位置，从而区分左右子树两部分。
    """

    def build(index, left, right) -> TreeNode:
        if index > len(preorder) - 1 or left > right:
            return None
        val = preorder[index]
        root = TreeNode(val)
        # 注意这里要再次判断，防止 index 越界或者 left, right 没有及时收敛
        if index == len(preorder) - 1 or left == right:
            return root
        i = postorder.index(preorder[index + 1])
        root.left = build(index + 1, left, i)
        root.right = build(index + 1 + i - left + 1, i + 1, right - 1)
        return root

    return build(0, 0, len(postorder) - 1)

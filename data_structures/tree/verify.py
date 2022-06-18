# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

from typing import List


def verify_postorder(postorder: List[int]) -> bool:
    """
    根据后序遍历重建 BST，因为倒序遍历数组，所以是根 -> 右 -> 左的顺序。
    如果是验证前序遍历，那么就正序遍历数组，以 根 -> 左 -> 右的顺序。
    时间复杂度 O(n)
    空间复杂度 O(n)
    """

    def verify(lower, upper) -> None:
        nonlocal index
        if index < 0:
            return
        val = postorder[index]
        if not lower < val < upper:
            return
        index -= 1
        verify(val, upper)
        verify(lower, val)

    index = len(postorder) - 1
    verify(-float("inf"), float("inf"))
    return index == -1


# 给定一个 无重复元素 的整数数组 preorder ， 如果它是以二叉搜索树的先序遍历排列 ，返回 true 。


def verify_preorder(preorder: List[int]) -> bool:
    def build(lower, upper):
        nonlocal index
        if index > len(preorder) - 1:
            return
        val = preorder[index]
        if not lower < val < upper:
            return
        index += 1
        build(lower, val)
        build(val, upper)

    index = 0
    build(-float("inf"), float("inf"))
    return index == len(preorder)


# NOTES: 前序/后序遍历 BST 也是一样的思路，只是要实际构造出 TreeNode

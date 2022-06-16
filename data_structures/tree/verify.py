# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

from typing import List


def verify_postorder(postorder: List[int]) -> bool:
    """
    根据后序遍历重建 BST，因为倒序遍历数组，所以是根 -> 右 -> 左的顺序。
    如果是验证前序遍历，那么就正序遍历数组，以 根 -> 左 -> 右的顺序。
    时间复杂度 O(n)
    空间复杂度 O(n)
    """

    def verify(postorder, low, high) -> None:
        if not postorder:
            return
        val = postorder[-1]
        if not low < val < high:
            return
        postorder.pop()
        verify(postorder, val, high)
        verify(postorder, low, val)

    verify(postorder, -float("inf"), float("inf"))
    return not postorder


# 给定一个 无重复元素 的整数数组 preorder ， 如果它是以二叉搜索树的先序遍历排列 ，返回 true 。


def verify_preorder(preorder: List[int]) -> bool:
    def build(low, high):
        if not vals:
            return
        if not low < vals[-1] < high:
            return
        val = vals.pop()
        build(low, val)
        build(val, high)

    # 使用倒序来避免 pop(0) 的高成本
    vals = preorder[::-1]
    build(-float("inf"), float("inf"))
    return vals == []


# TODO: 单调栈解法

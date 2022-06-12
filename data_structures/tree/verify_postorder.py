# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

from typing import List


def verify_postorder(postorder: List[int]) -> bool:
    """
    根据后序遍历重建 BST，因为倒序遍历数组，所以是根 -> 右 -> 左的顺序。
    如果是验证前序遍历，那么就正序遍历数组，以 根 -> 左 -> 右的顺序。
    时间复杂度 O(n)
    空间复杂度 O(n)
    """

    def verify(postorder, min, max) -> None:
        if not postorder:
            return
        val = postorder[-1]
        if not min < val < max:
            return
        postorder.pop()
        verify(postorder, val, max)
        verify(postorder, min, val)

    verify(postorder, -float("inf"), float("inf"))
    return not postorder

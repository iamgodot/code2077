def verify_postorder(postorder: list[int]) -> bool:
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


# Verify Preorder Sequence in Binary Search Tree
# https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/description/


def verify_preorder(preorder: list[int]) -> bool:
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

# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。


# 最后一个元素是根节点，前面应当可以分为两部分，前半部分小于根节点，后半部分大于根节点
# 时间复杂度 O(n^2) 空间复杂度最坏情况下 O(n)
def verify_postorder(postorder: List[int]) -> bool:
    def verify(left, right) -> bool:
        if left >= right:
            return True
        val = postorder[right]
        i = left
        while postorder[i] < val:
            i += 1
        for num in postorder[i:right]:
            if num < val:
                return False

        return verify(left, i - 1) and verify(i, right - 1)

    if not postorder:
        return True
    return verify(0, len(postorder) - 1)

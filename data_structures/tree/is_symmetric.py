# 给定一个二叉树，检查它是否是镜像对称的。
from tree import TreeNode


# 两种实现的时间和空间复杂度都是 O(n)
def check(root: TreeNode) -> bool:
    if not root:
        return True

    def _check(left: TreeNode, right: TreeNode):
        if not left or not right:
            return left is right
        return (
            left.val == right.val
            and _check(left.left, right.right)
            and _check(left.right, right.left)
        )

    return _check(root.left, root.right)


# 其实不一定要用队列，只要保证需要检查的元素一对一对进入容器，栈也可以实现
# 层序遍历也可以实现，先全部遍历出来然后对半检查即可
def check_it(root: TreeNode) -> bool:
    if not root:
        return True
    from collections import deque

    dq = deque([root.left, root.right])
    while dq:
        left, right = dq.pop(), dq.pop()
        if not left or not right:
            if left is not right:
                return False
        elif left.val != right.val:
            return False
        else:
            dq.appendleft(left.left)
            dq.appendleft(right.right)
            dq.appendleft(left.right)
            dq.appendleft(right.left)

    return True


if __name__ == "__main__":
    root1 = TreeNode(
        val=1,
        left=TreeNode(val=2, left=TreeNode(3), right=TreeNode(4)),
        right=TreeNode(val=2, left=TreeNode(4), right=TreeNode(3)),
    )
    # 1
    # | \
    # 2  2
    # |\ |\
    # 3 44 3
    root2 = TreeNode(
        val=1,
        left=TreeNode(val=2, right=TreeNode(3)),
        right=TreeNode(val=2, right=TreeNode(3)),
    )
    # 1
    # | \
    # 2  2
    #  \  \
    #   3  3
    for method in [check, check_it]:
        assert method(root1) is True
        assert method(root2) is False

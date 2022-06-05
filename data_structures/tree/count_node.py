# 树 的根节点 root ，求出该树的节点个数。
# 完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，
# 并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。

from data_structures.tree import TreeNode


def count(root: TreeNode) -> int:
    """
    对于满二叉树，节点数量等于 2^h - 1
    迭代的逻辑就是基于对树是否已满的判断：
    1. 如果满足，则按照公式直接计算
    2. 否则分别计算左子树和右子树，因为到一定深度肯定会满足条件（单个节点也可以看作满二叉树）

    因为递归，所以空间复杂度为 O(logn)，而每次递归判断深度也会循环 logn 的次数，所以时间复杂度为 O(logn*logn)，空间复杂度为 O(logn)，可以用二分法优化为 O(1)

    普通的二叉树遍历方式的时间和空间复杂度都是 O(n)
    """
    if not root:
        return 0

    def count_level(node):
        level = 0
        while node:
            level += 1
            node = node.left
        return level

    left = count_level(root.left)
    right = count_level(root.right)

    if left == right:
        return 2 ** left + count(root.right)
    else:
        return 2 ** right + count(root.left)


if __name__ == "__main__":
    # 1
    # | \
    # 2  3
    # |\ |
    # 4 56
    root = TreeNode(
        val=1,
        left=TreeNode(val=2, left=TreeNode(val=4), right=TreeNode(5)),
        right=TreeNode(val=3, left=TreeNode(val=6)),
    )
    assert count(root) == 6

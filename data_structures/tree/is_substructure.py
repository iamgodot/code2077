# 输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
# B是A的子结构， 即 A中有出现和B相同的结构和节点值。

from data_structures.tree import TreeNode


# 时间复杂度 O(m*n) 其中 m,n 分别为 A,B 的节点数量
# 空间复杂度 O(m) 最坏情况下 A 退化为链表，此时总递归深度为 m
def is_substructure(A: TreeNode, B: TreeNode) -> bool:
    def is_similar(a, b):
        if not a or not b:
            return a is b if not a else True
        return (
            a.val == b.val
            and is_similar(a.left, b.left)
            and is_similar(a.right, b.right)
        )

    if not A or not B:
        return False

    return is_similar(A, B) or is_substructure(A.left, B) or is_substructure(A.right, B)


if __name__ == "__main__":
    a = TreeNode(
        val=3,
        left=TreeNode(val=4, left=TreeNode(1), right=TreeNode(2)),
        right=TreeNode(5),
    )
    b = TreeNode(4, left=TreeNode(1))
    assert is_substructure(a, b) is True

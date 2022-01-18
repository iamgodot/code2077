# 翻转一棵二叉树。
from data_structures.tree import TreeNode, levelorder


# 注意需要返回 root 节点
# 不管是递归还是迭代都要考虑好使用何种遍历，
# 比如这里用的是前序遍历
def invert(root: TreeNode):
    if not root:
        return root
    root.left, root.right = root.right, root.left
    invert(root.left)
    invert(root.right)

    return root


def invert_it(root: TreeNode):
    stack = []
    cur = root
    while cur or stack:
        if cur:
            cur.left, cur.right = cur.right, cur.left
            stack.append(cur.right)
            cur = cur.left
        else:
            cur = stack.pop()

    return root


if __name__ == "__main__":
    for method in [invert, invert_it]:
        root = TreeNode(
            val=4,
            left=TreeNode(val=2, left=TreeNode(1), right=TreeNode(3)),
            right=TreeNode(val=7, left=TreeNode(6), right=TreeNode(9)),
        )
        # Before invert
        # 4
        # | \
        # 2  7
        # |\ |\
        # 1 36 9
        # After invert
        # 4
        # | \
        # 7  2
        # |\ |\
        # 9 63 1
        res = levelorder(method(root))
        assert [i for j in res for i in j] == [4, 7, 2, 9, 6, 3, 1]

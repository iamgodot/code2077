# 路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。
# 同一个节点在一条路径序列中 至多出现一次 。
# 该路径 至少包含一个 节点，且不一定经过根节点。
# 路径和 是路径中各节点值的总和。
# 给你一个二叉树的根节点 root ，返回其 最大路径和 。

from tree import TreeNode


# 先看对任意一个节点，如何从两边的长度选择更长的一条
# 之后就是以根节点开始遍历整棵树，保留最大的（左边 + 节点 + 右边）和
# 时间复杂度为 O(n)，因为要遍历整棵树
# 空间复杂度最坏为 O(n)，在树完全失衡的情况下递归
def max_path_sum(root: TreeNode) -> int:
    res = -float("inf")

    def max_edge(node: TreeNode) -> int:
        if not node:
            return 0

        edge_left = max(max_edge(node.left), 0)
        edge_right = max(max_edge(node.right), 0)

        nonlocal res  # 注意这里更新 res 的话必须显式声明使用 outer var
        res = max(res, node.val + edge_left + edge_right)

        return node.val + max(edge_left, edge_right)

    max_edge(root)

    return int(res)


if __name__ == "__main__":
    root = TreeNode(val=1, left=TreeNode(2), right=TreeNode(3))
    assert max_path_sum(root) == 6
    root = TreeNode(
        val=-10,
        left=TreeNode(9),
        right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)),
    )
    assert max_path_sum(root) == 42

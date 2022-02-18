# 路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。
# 同一个节点在一条路径序列中 至多出现一次 。
# 该路径 至少包含一个 节点，且不一定经过根节点。
# 路径和 是路径中各节点值的总和。
# 给你一个二叉树的根节点 root ，返回其 最大路径和 。

from data_structures.tree import TreeNode

# 先看对任意一个节点，如何从两边的长度选择更长的一条
# 之后就是以根节点开始遍历整棵树，保留最大的（左边 + 节点 + 右边）和
# 时间复杂度为 O(n)，因为要遍历整棵树
# 空间复杂度最坏为 O(n)，在树完全失衡的情况下递归

# 定义 max_edge 来寻找一个节点带来的最大路径和，这种情况下，返回的路径必然包含此节点本身
# 那么 max_path_sum 求最大路径和对于一个节点代表的树来说，有四种情况：
# 1. 只有节点本身
# 2. 节点 + 左子树路径
# 3. 节点 + 右子树路径
# 4. 节点 + 左子树路径 + 右子树路径
# 还有不含当前节点的左右子树两种情况在 max_edge 的递归过程中已经隐含了，所以不需要再考虑
# 因此关键在于
# 1. 取 edge_left 和 edge_right 的时候通过与 0 取 max 来涵盖四种情况
# 2. 更新 res 时一定要加上 node.val（原因是上面的递归隐含）
# 3. 注意使用 nonlocal 来更新 res
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

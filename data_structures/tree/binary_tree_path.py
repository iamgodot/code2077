# 二叉树的所有路径
# 给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。
# 叶子节点 是指没有子节点的节点。

from typing import List

from data_structures.tree import TreeNode


# 时间复杂度 O(n^2) 对于 O(n) 条路径每条都会做 O(n) 的 join 操作
# 空间复杂度 O(n^2) res 需要 O(n^2) 大小，递归深度 O(h) 最坏情况下为 O(n)
def binary_tree_path(root: TreeNode) -> List[str]:
    def dfs(node):
        if not node:
            return
        path.append(str(node.val))  # 注意要转换为字符串
        if not node.left and not node.right:
            res.append("->".join(path))
        dfs(node.left)
        dfs(node.right)
        path.pop()

    path, res = [], []
    dfs(root)
    return res


# 路径总和
# 给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。如果存在，返回 true ；否则，返回 false 。


# 时间复杂度 O(n)
# 空间复杂度 O(h) h 为树的高度，最坏情况下 h=n
def has_path_sum(root: TreeNode, target_sum: int) -> bool:
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == target_sum
    return has_path_sum(root.left, target_sum - root.val) or has_path_sum(
        root.right, target_sum - root.val
    )


# 路径总和 II
# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。


# 时间复杂度 O(n^2) 对于 O(n) 条路径每次要做 O(n) 的 append 操作
# 空间复杂度 O(n^2) res 需要 O(n^2) 大小，递归深度 O(h) 最坏情况下为 O(n)
def path_sum(root: TreeNode, target_sum: int) -> List[List[int]]:
    def dfs(node: TreeNode, target: int):
        if not node:
            return
        path.append(node.val)  # 注意这里是先 append 再下面做判断
        if not node.left and not node.right and node.val == target:
            res.append(path[:])
        dfs(node.left, target - node.val)
        dfs(node.right, target - node.val)
        path.pop()

    path, res = [], []
    dfs(root, target_sum)
    return res


# 路径总和 III
# 给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
# 路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。


# 时间复杂度 O(n^2) 对于每个节点为起点都需要 O(n) 来搜索路径
# 空间复杂度 O(n) 递归深度最坏情况下为 n
def path_sum2(root: TreeNode, target_sum: int) -> int:
    def dfs(node, target) -> int:
        if not node:
            return 0
        res = 0
        if node.val == target:
            res += 1
        return (
            res + dfs(node.left, target - node.val) + dfs(node.right, target - node.val)
        )

    if not root:
        return 0
    res = dfs(root, target_sum)
    return (
        res + self.pathSum(root.left, target_sum) + self.pathSum(root.right, target_sum)
    )

from typing import List

from data_structures.tree import TreeNode

# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

# 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。


def rob(nums: List[int]) -> int:
    """
    dp[i] 定义为 i 位置偷窃到的最高金额。

    每个位置（房屋）都存在偷或者不偷两种情况，所以：
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    """
    pre, cur = 0, nums[0]
    for i in range(1, len(nums)):
        pre, cur = cur, max(pre + nums[i], cur)
    return cur


# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。

# 给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。


def rob(nums: List[int]) -> int:
    """
    思路和上面类似，只是要单独考虑首尾节点的情况。

    1. 考虑（注意是考虑不是选择）首节点 + 不考虑尾节点
    2. 考虑尾节点 + 不考虑首节点
    """

    def _rob(nums) -> int:
        pre, cur = 0, nums[0]
        for i in range(1, len(nums)):
            pre, cur = cur, max(pre + nums[i], cur)
        return cur

    if len(nums) == 1:
        return nums[0]
    return max(_rob(nums[:-1]), _rob(nums[1:]))


# 小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为 root 。

# 除了 root 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果 两个直接相连的房子在同一天晚上被打劫 ，房屋将自动报警。

# 给定二叉树的 root 。返回 在不触动警报的情况下 ，小偷能够盗取的最高金额 。


def rob(root: TreeNode) -> int:
    """
    需要后序遍历来判断整个二叉树的最佳策略。

    对于每个节点，都存在抢和不抢两种情况：
        如果抢：则左右子节点不可以抢
        如果不抢：则左右子节点（分别）可以抢或者不抢
    """

    def rob_node(node: TreeNode) -> List[int]:
        if not node:
            return [0, 0]

        rob_left = rob_node(node.left)
        rob_right = rob_node(node.right)

        max_with_node = node.val + rob_left[1] + rob_right[1]
        max_without_node = max(rob_left) + max(rob_right)
        return [max_with_node, max_without_node]

    return max(rob_node(root))

from data_structures.tree import TreeNode


# House Robber
# https://leetcode.com/problems/house-robber/


def rob(nums: list[int]) -> int:
    """
    dp[i] = max(dp[i-1], dp[i-2] + nums[i])

    Time: O(n)
    Space: O(1)
    """
    pre, cur = 0, nums[0]
    for i in range(1, len(nums)):
        pre, cur = cur, max(pre + nums[i], cur)
    return cur


# House Robber II
# https://leetcode.com/problems/house-robber-ii/


def rob(nums: list[int]) -> int:
    """
    Consider 2 cases, choosing either the first or the last house.

    Time: O(n)
    Space: O(1)
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

    def rob_node(node: TreeNode) -> list[int]:
        if not node:
            return [0, 0]

        rob_left = rob_node(node.left)
        rob_right = rob_node(node.right)

        max_with_node = node.val + rob_left[1] + rob_right[1]
        max_without_node = max(rob_left) + max(rob_right)
        return [max_with_node, max_without_node]

    return max(rob_node(root))

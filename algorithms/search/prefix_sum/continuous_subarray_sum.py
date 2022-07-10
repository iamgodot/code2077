# 给你一个整数数组 nums 和一个整数 k ，编写一个函数来判断该数组是否含有同时满足下述条件的连续子数组：

# 子数组大小 至少为 2 ，且
# 子数组元素总和为 k 的倍数。
# 如果存在，返回 true ；否则，返回 false 。

# 如果存在一个整数 n ，令整数 x 符合 x = n * k ，则称 x 是 k 的一个倍数。0 始终视为 k 的一个倍数。


from typing import List


def check(nums: List[int], k: int) -> bool:
    """
    Time: O(n)
    Space: O(min(n, k))
    """
    # key 为前缀和对 k 的余数，value 为下标
    hashtable = {0: -1}
    remain = 0
    for i in range(len(nums)):
        remain = (remain + nums[i]) % k
        if remain in hashtable:
            if i - hashtable[remain] > 1:
                return True
        else:
            hashtable[remain] = i
    return False


if __name__ == "__main__":
    assert check([23, 2, 4, 6, 7], 6) is True
    assert check([23, 2, 6, 4, 7], 13) is False

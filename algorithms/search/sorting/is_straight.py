# 从若干副扑克牌中随机抽 5 张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。


# 注意大小王只有两张，所以 0 只可能出现 0/1/2 三种情况
# 只要满足剩下的牌不重复并且 max - min < 5 即可成为顺子
# 时间复杂度 O(n*logn) 为排序成本，其中 n 为 5，空间复杂度 O(1)
def is_straight(self, nums: List[int]) -> bool:
    jokers = 0
    nums.sort()
    for i in range(4):
        if nums[i] == 0:
            jokers += 1
            continue
        if nums[i] == nums[i + 1]:
            return False

    return nums[-1] - nums[jokers] < 5


if __name__ == "__main__":
    assert is_straight([1, 2, 3, 4, 5]) is True
    assert is_straight([0, 0, 1, 2, 5]) is True

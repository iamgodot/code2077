# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。

from math import sqrt


# 利用双端指针可以一次遍历完成，右端的起点从 c 的平方根开始
# 时间复杂度为 O(sqrt(c))
def judge_square_sum(c: int) -> bool:
    a, b = 0, int(sqrt(c))
    while a <= b:
        sum_ = a * a + b * b
        if sum_ < c:
            a += 1
        elif sum_ > c:
            b -= 1
        else:
            return True

    return False


if __name__ == "__main__":
    assert judge_square_sum(5) is True
    assert judge_square_sum(4) is True
    assert judge_square_sum(3) is False

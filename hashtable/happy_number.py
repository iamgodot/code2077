# 编写一个算法来判断一个数 n 是不是快乐数。
# 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
# 然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。
# 如果可以变为 1，那么这个数就是快乐数。


def _find_next(n: int) -> int:
    res = 0

    while n > 0:
        n, last_digit = divmod(n, 10)
        res += last_digit**2

    return res


# 1. Use hashtable: 时间复杂度 O(logn)，因为要处理数字的每一位，而位数由 logn 决定，空间复杂度 O(logn)
def is_happy_with_set(n: int) -> bool:
    nums = set()

    while n != 1 and n not in nums:
        nums.add(n)
        n = _find_next(n)

    return n == 1


# 2. Use two pointers: 时间复杂度 O(logn)，空间复杂度 O(1)
def is_happy_with_two_pointers(n: int) -> bool:
    slow, fast = n, _find_next(n)  # 这里如果 slow=fast=n 会影响 while loop

    while fast != 1 and slow != fast:
        slow = _find_next(slow)
        fast = _find_next(_find_next(fast))

    return fast == 1


if __name__ == '__main__':
    for method in [is_happy_with_set, is_happy_with_two_pointers]:
        assert method(19) is True
        assert method(2) is False

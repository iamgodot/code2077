# 给定一个正整数 n ，输出外观数列的第 n 项。
# 「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。


def find_next1(num: str) -> str:
    recorded = ""
    cur, count = num[0], 1
    for char in num[1:]:
        if char == cur:
            count += 1
            continue
        recorded += f"{count}{cur}"
        cur = char
        count = 1
    return f"{recorded}{count}{cur}"


def find_next2(num: str) -> str:
    recorded = ""
    start = cur = 0
    size = len(num)
    while cur < size:
        while cur < size and num[start] == num[cur]:
            cur += 1
        recorded += str(cur - start) + num[start]
        start = cur
    return recorded


def count_and_say(n: int, find_next_func: callable) -> str:
    num = "1"
    for _ in range(n - 1):
        num = find_next_func(num)
    return num


if __name__ == "__main__":
    for func in find_next1, find_next2:
        for n, num in (1, "1"), (4, "1211"):
            assert count_and_say(n, func) == num

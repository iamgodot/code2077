# Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/description


def daily_temperatures(temperatures: list[int]) -> list[int]:
    stack = []
    length = len(temperatures)
    res = [0 for _ in range(length)]
    for i in range(length - 1, -1, -1):
        while stack and temperatures[stack[-1]] <= temperatures[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1] - i
        stack.append(i)
    return res


if __name__ == "__main__":
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [
        1,
        1,
        4,
        2,
        1,
        1,
        0,
        0,
    ]

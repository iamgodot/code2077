from typing import List


def open_lock(deadends: List[str], target: str) -> int:
    """
    Start from '0000'.
    BFS:
        Based on '0000', there're 8 choices for which there're also 8 choices for each.
        During the searching, we can also use a Set and deadends to filter.
        If target is to be reached, return steps.
    Edge cases:
        1. If '0000' in deadends, return -1
        2. If target is '0000', return 0
    Complexity:
        Time: O(b^d * d^2 + m*d) b is 10, d is 4 and m is the length of deadends
        Space: O(b^d * d + m)
    """
    if "0000" in deadends:
        return -1
    if target == "0000":
        return 0

    set_ = set(deadends).union({"0000"})
    from collections import deque

    dq = deque([("0000", 0)])

    def _get_next_char(char: str, reverse=False) -> str:
        if reverse:
            return str(int(char) - 1 if char != "0" else 9)
        else:
            return str(int(char) + 1 if char != "9" else 0)

    def get_next_comb(comb: str) -> str:
        chars = list(comb)
        for i in range(4):
            for rev in [True, False]:
                char = chars[i]
                chars[i] = _get_next_char(char, rev)
                yield "".join(chars)
                chars[i] = char

    while dq:
        combination, steps = dq.pop()
        for comb_next in get_next_comb(combination):
            if comb_next == target:
                return steps + 1
            if comb_next in set_:
                continue
            dq.appendleft((comb_next, steps + 1))
            set_.add(comb_next)

    return -1


if __name__ == "__main__":
    assert open_lock(["0201", "0101", "0102", "1212", "2002"], "0202") == 6
    assert open_lock(["0000"], "0202") == -1
    assert open_lock([], "0000") == 0

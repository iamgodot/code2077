# 编写一个程序，通过填充空格来解决数独问题。

# 数独的解法需 遵循如下规则：

# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
# 数独部分空格内已填入了数字，空白格用 '.' 表示。


from typing import List


# 类似排列的思路，注意可以利用横纵坐标的和/差在对角线不变来判断斜线方向上是否有冲突
# 时间复杂度 O(n!) 空间复杂度 O(n)
def solve(n: int) -> List[List[str]]:
    def gen_result(path) -> List[str]:
        res = []
        for i in range(n):
            row = ["." for _ in range(n)]
            row[path[i]] = "Q"
            res.append("".join(row))

        return res

    def bt():
        if len(path) == n:
            res.append(gen_result(path))
            return
        row = len(path)
        for col in range(n):
            sum_, subtraction = row + col, row - col
            if col in path or sum_ in diagonals[0] or subtraction in diagonals[1]:
                continue
            path.append(col)
            diagonals[0].append(sum_)
            diagonals[1].append(subtraction)
            bt()
            path.pop()
            diagonals[0].pop()
            diagonals[1].pop()

    res, path = [], []
    diagonals = [[], []]  # sums, subtractions
    bt()
    return res


if __name__ == "__main__":
    assert solve(4) == [
        [".Q..", "...Q", "Q...", "..Q."],
        ["..Q.", "Q...", "...Q", ".Q.."],
    ]

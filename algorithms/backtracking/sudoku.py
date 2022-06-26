# 编写一个程序，通过填充空格来解决数独问题。

# 数独的解法需 遵循如下规则：

# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
# 数独部分空格内已填入了数字，空白格用 '.' 表示。


from typing import List


# 一个比较粗略的时间复杂度上限为 O(9 ^ 9*9)，即 9x9 个格子，每个都有 1-9 种选择
def solve(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """

    def bt(start: int):
        nonlocal is_finished

        if start == len(blanks):
            is_finished = True
            return

        i, j = blanks[start]
        for num in range(1, 10):
            index = num - 1
            if (
                nums_in_rows[index][i]
                or nums_in_columns[index][j]
                or nums_in_matrix[index][i // 3][j // 3]
            ):
                continue

            board[i][j] = str(num)
            nums_in_rows[index][i] = nums_in_columns[index][j] = nums_in_matrix[index][
                i // 3
            ][j // 3] = 1
            bt(start + 1)

            if is_finished:
                return

            board[i][j] = "."
            nums_in_rows[index][i] = nums_in_columns[index][j] = nums_in_matrix[index][
                i // 3
            ][j // 3] = 0

    nums_in_rows = [[0 for _ in range(9)] for _ in range(9)]
    nums_in_columns = [[0 for _ in range(9)] for _ in range(9)]
    nums_in_matrix = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(9)]
    blanks = []  # (i, j)
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                blanks.append((i, j))
                continue
            num = int(board[i][j])
            nums_in_rows[num - 1][i] = 1
            nums_in_columns[num - 1][j] = 1
            nums_in_matrix[num - 1][i // 3][j // 3] = 1

    is_finished = False
    bt(0)


if __name__ == "__main__":
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    solve(board)
    assert board == [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
    ]

# Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/


def isValidSudoku(board: list[list[str]]) -> bool:
    """
    Time: O(n^2)
    Space: O(n^2)
    """
    row_sets = [set() for _ in range(9)]
    col_sets = [set() for _ in range(9)]
    box_sets = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            val = board[i][j]
            if val == ".":
                continue
            if val in row_sets[i]:
                return False
            row_sets[i].add(val)
            if val in col_sets[j]:
                return False
            col_sets[j].add(val)
            box_set = box_sets[i // 3 * 3 + j // 3]
            if val in box_set:
                return False
            box_set.add(val)
    return True

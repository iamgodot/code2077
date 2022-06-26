# 给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。

# 例如：

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...


def convert_to_title(columnNumber: int) -> str:
    """
    注意 index 是从 1 而不是 0 开始，所以每次都要把 columnNumber 减一
    时间复杂度：O(log26 columnNumber)
    """
    res = ""
    ord_base = ord("A")
    while columnNumber > 0:
        columnNumber, rem = divmod(columnNumber - 1, 26)
        res = chr(ord_base + rem) + res

    return res

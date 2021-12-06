# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。

# 除了加法过程中的进位，还需要注意最后结果的前面不能连续出现多个 0，比如 '00'
# 因为题目中说了非负整数，所以不用担心 num1 或 num2 为空字符串的情况
def add_strings(num1: str, num2: str) -> str:
    cur1, cur2 = len(num1) - 1, len(num2) - 1
    res = ""
    carry = 0
    while cur1 >= 0 or cur2 >= 0:
        val1 = int(num1[cur1]) if cur1 >= 0 else 0
        val2 = int(num2[cur2]) if cur2 >= 0 else 0
        carry, val = divmod(val1 + val2 + carry, 10)
        res = f"{val}{res}"
        cur1 -= 1
        cur2 -= 1

    if carry:
        res = f"{carry}{res}"

    while res[1:] and res[0] == "0":
        res = res[1:]

    return res


if __name__ == "__main__":
    for num1, num2, res in (
        ("11", "123", "134"),
        ("456", "77", "533"),
        ("0", "0", "0"),
    ):
        assert add_strings(num1, num2) == res

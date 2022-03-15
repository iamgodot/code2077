# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。

# 注意:不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。

# 提示：

# 1 <= s.length <= 3 * 105
# s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
# s 表示一个有效的表达式
# '+' 不能用作一元运算(例如， "+1" 和 "+(2 + 3)" 无效)
# '-' 可以用作一元运算(即 "-1" 和 "-(2 + 3)" 是有效的)
# 输入中不存在两个连续的操作符
# 每个数字和运行的计算将适合于一个有符号的 32位 整数


def calculate(s: str) -> int:
    """
    通过栈来维护当前括号层级的正负状态，初始化为 [1]
    因为 op 会通过栈顶元素来更新当前的正负操作
    """
    op, stack = 1, [1]
    res = index = 0
    length = len(s)
    while index < length:
        char = s[index]
        if char == " ":
            index += 1
        elif char == "+":
            op = stack[-1]
            index += 1
        elif char == "-":
            op = -stack[-1]
            index += 1
        elif char == "(":
            stack.append(op)
            index += 1
        elif char == ")":
            stack.pop()
            index += 1
        else:
            num = 0
            while index < length and "0" <= s[index] <= "9":
                num = num * 10 + int(s[index])
                index += 1
            res += num * op

    return res


if __name__ == "__main__":
    assert calculate("1 + 1") == 2
    assert calculate("2-1 + 2") == 3
    assert calculate("(1+(4+5+2)-3)+(6+8)") == 23

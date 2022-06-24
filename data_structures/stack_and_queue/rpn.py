# 根据 逆波兰表示法，求表达式的值。
# 有效的算符包括 +、-、*、/ 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
# 整数除法只保留整数部分。
# 给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。


# 思路简单，细节比较多
# 1. str 和 int 之间的类型转换
# 2. 除法的处理上面，需要保留整数部分
# 3. 最好确认参数为空的话要返回什么，None 还是 0
def eval_rpn(tokens: list) -> int:
    stack = []

    for token in tokens:
        if token in "+-*/":
            num2 = stack.pop()
            num1 = stack.pop()
            # 注意除法的处理，// 对于负数的情况是不正确的，比如 6//-132
            stack.append(int(eval(f"{num1}{token}{num2}")))
        else:
            stack.append(int(token))

    return stack.pop()


if __name__ == "__main__":
    for tokens, res in (
        (["18"], 18),
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
    ):
        assert eval_rpn(tokens) == res

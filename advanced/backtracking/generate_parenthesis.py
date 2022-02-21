# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。


# 在回溯的基础上，主要思路是提前生成有效的括号组合：
# 1. 如果 ( 的数量不足，则尝试添加左括号
# 2. 如果 ) 的数量小于 (，则尝试添加右括号
# 最后的时间复杂度的粗略上限为 O(2^2n * n) 这相当于 BruteForce 的时间复杂度
# 空间复杂度为 O(n)
def generate_parenthesis(n: int) -> list:
    res = []

    def bt(s):
        if len(s) == n * 2:
            res.append(s)
            return

        if s.count("(") < n:
            bt(s + "(")
        if s.count("(") > s.count(")"):
            bt(s + ")")

    bt("")
    return res


if __name__ == "__main__":
    assert generate_parenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]

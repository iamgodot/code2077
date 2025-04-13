# Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/description/


# 最后的时间复杂度的粗略上限为 O(2^2n * n) 这相当于 BruteForce 的时间复杂度
# 空间复杂度为 O(n)
def generate_parenthesis(n: int) -> list:
    """
    Time: O(2^2n * n)
    Space: O(n)
    """
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

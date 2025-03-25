# Basic Calculator
# https://leetcode.com/problems/basic-calculator/description/


def calculate(s: str) -> int:
    """Keep track of previous sign and update result when a new sign is found."""
    res = num = 0
    pre_sign = 1
    stack = []
    for char in s:
        if char == " ":
            continue
        if "0" <= char <= "9":
            num = num * 10 + int(char)
        if char in "+-":
            res += num * pre_sign
            num = 0
            pre_sign = -1 if char == "-" else 1
        if char == "(":
            stack.append(res)
            stack.append(pre_sign)
            # NOTE: no need to reset num
            res = 0
            pre_sign = 1
        if char == ")":
            res += num * pre_sign
            num = res
            pre_sign = stack.pop()
            res = stack.pop()
    res += num * pre_sign
    return res


# Basic Calculator II
# https://leetcode.com/problems/basic-calculator-ii/description/


def calculate2(s: str) -> int:
    stack = []
    num = 0
    pre_sign = "+"
    for i, char in enumerate(s):
        if "0" <= char <= "9":
            num = num * 10 + int(char)
        if char in "+-*/" or i == len(s) - 1:
            match (pre_sign):
                case "+":
                    stack.append(num)
                case "-":
                    stack.append(-num)
                case "*":
                    stack.append(stack.pop() * num)
                case "/":
                    stack.append(int(stack.pop() / num))
            num = 0
            pre_sign = char
    return sum(stack)


# Basic Calculator III
# https://leetcode.com/problems/basic-calculator-iii/description/
def calculate3(s: str) -> int:
    stack = []
    num = 0
    pre_sign = "+"
    s = s + " "
    for i, char in enumerate(s):
        if "0" <= char <= "9":
            num = num * 10 + int(char)
        if char in "+-*/)" or i == len(s) - 1:
            match (pre_sign):
                case "+":
                    stack.append(num)
                case "-":
                    stack.append(-num)
                case "*":
                    stack.append(stack.pop() * num)
                case "/":
                    stack.append(int(stack.pop() / num))
            num = 0
            pre_sign = char
            if char == ")":
                while isinstance(stack[-1], int):
                    num += stack.pop()
                pre_sign = stack.pop()
        if char == "(":
            stack.append(pre_sign)
            pre_sign = "+"
    return sum(stack)


if __name__ == "__main__":
    assert calculate("1 + 1") == 2
    assert calculate("2-1 + 2") == 3
    assert calculate("(1+(4+5+2)-3)+(6+8)") == 23

# 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
# 由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
# 注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。

# 1. 根据人脑思考过程可以联想到在 1 和 x 之间通过二分法查找
# 因为结果只需要返回整数，所以在出现小数时就可以停止
# 时间复杂度为 O(logn)，空间复杂度 O(1)
def sqrt(x: int) -> int:
    """
    因为 x 为非负整数，所以要考虑到 x 为 0，还有 x 为 1 的情况
    """
    low, high = 1, x
    while low <= high:
        mid = low + (high - low) // 2
        square = mid * mid
        if square == x:
            return mid
        elif square < x:
            low = mid + 1
        else:
            high = mid - 1
    return int(high)


# 2. 还有一种牛顿迭代法的解法，类似二分，时间复杂度也是 O(logn)，不过效率要更高
# 重点在于先找出函数方程式，f(x) = x^2 - C，目的是找到函数的零点，此时 x^2 = C，x 就是平方根
# 先随便找到函数曲线上一点，比如 Xi，然后沿着这一点画出切线与横轴的交点，把交点的横坐标作为新的 X 值
# 依次逼近，最终会距离算术平方根很近。核心是找到 X 的变化关系，即得到 X0 之后，如果计算 X1.
# 切线经过点(X0, X0^2 - C) 和点(X1, 0)，因为曲线关系为 y = x^2 - C 所以切线斜率为 2X0，
# 有直线方程式 k = (y1 - y0) / (x1 - x0)，所以可得 2X0 = (X0^2 - C) / (X0 - X1)，最终得到 X0 与 X1 的关系式
# X1 = 0.5*(C/X0 + X0)
def sqrt(x: int) -> int:
    if x == 0:
        return 0
    x0 = x
    while True:
        x1 = 0.5 * (x / x0 + x0)
        if abs(x1 - x0) < 1e-7:
            break
        x0 = x1
    return int(x1)


if __name__ == "__main__":
    assert sqrt(0) == 0
    assert sqrt(1) == 1
    assert sqrt(4) == 2
    assert sqrt(8) == 2

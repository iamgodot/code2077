# 在一条单行道上，有 n 辆车开往同一目的地。目的地是几英里以外的 target 。
# 给定两个整数数组 position 和 speed ，长度都是 n ，其中 position[i] 是第 i 辆车的位置， speed[i] 是第 i 辆车的速度(单位是英里/小时)。
# 一辆车永远不会超过前面的另一辆车，但它可以追上去，并与前车 以相同的速度 紧接着行驶。此时，我们会忽略这两辆车之间的距离，也就是说，它们被假定处于相同的位置。
# 车队 是一些由行驶在相同位置、具有相同速度的车组成的非空集合。注意，一辆车也可以是一个车队。
# 即便一辆车在目的地才赶上了一个车队，它们仍然会被视作是同一个车队。
# 返回到达目的地的 车队数量 。


from typing import List


def car_fleet(target: int, position: List[int], speed: List[int]) -> int:
    """
    通过栈来比较两辆车达到目的地的时间，注意要保留较慢的那个（即被追上的前车），
    另外要注意条件：一辆车永远不会超过前面的另一辆车。

    Time: O(n*logn) for sorting
    Space: O(n)
    """
    stack = []
    for p, s in sorted(zip(position, speed), reverse=True):
        time = float((target - p) / s)
        if stack and stack[-1] >= time:
            continue
        stack.append(time)
    return len(stack)


if __name__ == "__main__":
    assert car_fleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3

# 栈

栈是一种非常经典的数据结构，也应用在许多方面，比如递归调用、词法分析、Linux 目录和浏览器历史记录等。它的接口主要有 push/pop/top/empty，最重要的特性在于数据是 LIFO 的，即最先进入的在栈底，而最后进入的在栈顶。

队列恰好与栈相反，第一个从队尾进队的元素，也会第一个从队首出队。接口接口为 push/pop/peek/empty。另外队列还分为单向和双向，后者的两端都可以做入队和出队的操作。

Python 的 list 可以很方便地模拟栈和队列的操作，然而，collections.deque 模块的 appendleft/popleft 要比 list 的 insert(0, val)/pop(0) 效率高很多，前者为 O(1)，后者为 O(n)，参考 [Stackoverflow](https://stackoverflow.com/questions/23487307/python-deque-vs-list-performance-comparison)。

1. [利用栈实现队列](stacks_for_queue.py)
2. [利用队列实现栈](queues_for_stack.py)
3. [最小栈](min_stack.py)
4. [有效的括号](valid_parentheses.py)
5. [删除字符串中所有相邻重复项](remove_duplicates.py)
6. [逆波兰表达式求值](rpn.py)
7. [栈的推入、弹出序列](validate_stack_seq.py)
8. [车队](car_fleet.py)
9. [基本计算器](calculator.py)

## 单调栈

单调栈主要用来在 O(n) 时间寻找上/下一个更小/大的元素。

1. [每日温度](daily_temperatures.py)
2. [下一个更大元素](next_greater_element.py)
3. [柱状图中最大的矩形](largest_rectangle.py)
4. [接雨水](algorithms/dynamic_programming/trapping_rain_water.py)

### Next greater element

遍历方向：从后向前，这样保证了每个元素后面的部分已经处理，这是由 next 决定的。
整个过程中保证栈是单调递增的，上小下大，这是由 greater 决定的。

1. 如果栈不为空且栈顶元素小于等于（等于是必要的，因为可能涉及到下标的更新）当前元素，不断 pop。原因是如果栈顶元素比自己还小，那么完全可以被当前元素取代。
2. 如果栈中存在更大元素，则进行设置，注意这里设置的既可以是元素值也可以是下标。
3. 将当前元素（值或下标）保存进栈。

### Next smaller element

1. 从后向前遍历
2. 如果栈顶元素大于等于当前元素则 pop；单调递减栈，上大下小

### Last greater element

1. 从前向后遍历
2. 如果栈顶元素小于等于当前元素则 pop；单调递增栈，上小下大

### Last smaller element

1. 从前向后遍历
2. 如果栈顶元素大于等于当前元素则 pop；单调递减栈，上大下小

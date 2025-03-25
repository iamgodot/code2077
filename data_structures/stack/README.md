# Stack & Queue

In Python, list can be used to simulate stack and queue, but collections.deque is more efficient than list, because appendleft/popleft is O(1) while insert(0, val)/pop(0) is O(n), see [Stackoverflow](https://stackoverflow.com/questions/23487307/python-deque-vs-list-performance-comparison).

## Stack

1. [Valid Parentheses](valid_parentheses.py)
1. [Implement Queue using Stacks](stacks_for_queue.py)
1. [Implement Stack using Queues](queues_for_stack.py)
1. [Min Stack](min_stack.py)
1. [Evaluate Reverse Polish Notation](rpn.py)
1. [Basic Calculator](calculator.py)
1. [实现循环队列](design_circular_queue.py)
1. [删除字符串中所有相邻重复项](remove_duplicates.py)
1. [栈的推入、弹出序列](validate_stack_seq.py)
1. [车队](car_fleet.py)

## Mono stack

A monotonic stack is used to find the next smaller/greater element in O(n) time.

**Make sure of what to store in the stack, which could be the index or the value.**

- Traverse order
  - From back to front: next greater/smaller element
  - From front to back: last greater/smaller element
- Stack pop condition
  - If stack top is smaller or equal to current element: next/last greater element
  - If stack top is greater or equal to current element: next/last smaller element

1. [Daily Temperatures](daily_temperatures.py)
1. [Next Greater Element I && II](next_greater_element.py)
1. [Largest Rectangle in Histogram](largest_rectangle.py)

## Mono queue

1. [Sliding Window Maximum](algorithms/search/sliding_window/sliding_window_maximum.py)

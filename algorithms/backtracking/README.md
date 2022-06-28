# 回溯

回溯的本质是穷举，其实和 Bruteforce 一样，但有时候没办法在一开始就确定需要循环的总次数，所以在回溯中利用递归来解决。

在 Top-down 的递归过程中，到达最底层调用之后会逐层返回上层的函数，这一步骤称之为回溯。通过回溯，可以穷举所有的可能性，对于某些复杂问题，这是唯一的解决方法。由此也可以看出，回溯的复杂度并不低，类似 DFS，但过程中也可以通过剪枝来降低搜索的次数。

在回溯的过程中，主要涉及到横向和纵向两种分布。因为回溯可以看作是一种树形结构，所以横向指的就是对于某个节点，有多少个子节点需要遍历；而纵向表示每个子节点往下层延伸，到达叶子节点有多少层。横向代表了树的宽度，而纵向代表了树的深度。

实现的伪代码逻辑如下：

```python
def bt(*args, **kwargs):
    # Base case
    if sth:
        return
    # Iterate children nodes
    for i in elements:
        # Process
        do_sth(i)
        # Recursion
        bt(...)
        # Undo process
        undo_sth(i)
```

在循环中，递归调用之后，通过撤销之前的处理到检查所有可能性的效果，可以理解为到达一个叶子节点之后回到上一个父节点，再进入到一个新的叶子节点中。

实际编码中，是否要执行回退操作取决于参数是否为可变量，比如字符串就不需要撤销，而列表则必须要。

## 题目

回溯一般用于解决几类问题：

- 组合 combination
  - 回溯
    - 一般来说目标是组合的和达到 target，所以递归的停止条件也是 sum 的判断
    - 三部曲：操作 -> 递归 -> 撤销
  - 要点
    - 事先对 candidates 排序，这样在遍历过程中可以及时剪枝
    - 回溯时使用 start 作为遍历的起始下标，而是否可以重复选取元素决定了递归时 start 是否 +1
    - 如果 candidates 中存在重复元素，那么有可能造成结果中出现重复组合，比如 `[1, 1, 2, 3]`，可以在遍历过程中进行去重。但需要注意是在横向而不是纵向查重，这一点使用 i > start 来判断
    - 在递归返回时，向 res 添加结果序列的 copy 而不是序列本身
  - 复杂度
    - 时间：对于 n 个元素，每个都有 n 次选或不选的判断，所以一个比较宽松的上界是 O(n * 2^n)
    - 空间：O(n)，包括数组和递归栈的成本
  - 题目
    - 不重复的 candidates，可以重复选取同一个数字
    - 可能重复的 candidates，不可以重复选取（注意这里就需要做去重）
- 子集 subsets
  - 类似组合问题，因为结果也是不区分顺序的
  - 可以理解为在递归树中，组合只保存叶子节点，而子集会对所有的节点结果进行存储
- 排列 permutation
  - 回溯
    - 递归的停止条件是结果中使用了所有的数字
  - 要点
    - 因为是排列，所以无需排序
    - 为了记录已经使用过的元素，要额外创建 used 数组，遍历时如果碰到则跳过
    - 三部曲时要加入 used 数组的更新与撤销操作
    - 如果有重复元素则需要特殊处理
      - 首先要对 candidates 排序
      - 过程中有横向和纵向两种去重方式，横向的效率更高一些，判断条件要注意 used[i-1] 应当是 False
  - 复杂度
    - 时间：回溯涉及到 n! 次调用，每次的 copy 都是 O(n)，所以整体复杂度为 O(n! * n)
    - 空间：额外数组和递归栈的成本都是 O(n) 所以整体复杂度也是 O(n)
  - 题目
    - 不重复的数组返回所有的全排列
    - 可重复的数组返回所有不重复的全排列
- 棋盘：八皇后、数独
  - 需要想清楚递归的横向和纵向范围，比如对数独来说，横向是 1-9 个数字，纵向是所有的空白格子
  - 使用额外的数据结构/方法来辅助判断，比如八皇后中利用横纵坐标的和/差来判断对角线冲突；数独中利用额外的矩阵来判断一个数字是否已经出现在该行/列/小矩阵中
  - 对于数独这种 in-place 修改的要求，需要在回溯过程中利用 flag 判断并在撤销操作之前返回
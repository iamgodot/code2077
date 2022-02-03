# 二叉树

## 遍历

- DFS
  - 前序遍历（递归法、迭代法）：中左右，从上到下，求深度，真正体现回溯
  - 中序遍历（递归法、迭代法）：左中右，体现了 BST 的排序特点
  - 后序遍历（递归法、迭代法）：左右中，自底向上，求高度
- BFS 层序遍历（迭代法、队列）

## 题型分类

- 前序/后序
  - [翻转二叉树](invert.py)
  - [对称二叉树](is_symmetric.py)
  - [相同的树]()
  - [判断子结构](is_substructure.py)
  - [BST 的最近公共祖先](lowest_common_ancestor.py)
- 后序
  - [二叉树最大深度](depth.py)
  - [二叉树最小深度](depth.py)
  - [完全二叉树的节点个数（注意这题有更优化的解法）](count_node.py)
  - [平衡二叉树](balanced_tree.py)
  - [二叉树的最近公共祖先](lowest_common_ancestor.py)
  - [验证后序遍历](verify_postorder.py)
- 前序
  - [二叉树的所有路径]()
  - [路径总和 I/II/III](binary_tree_path.py)
  - [最大路径和](max_path_sum.py)
- 中序
  - [BST 的第 k 大节点](kth_largest.py)
  - [BST 与双向链表](tree_to_doubly_list.py)
- 构造
  - [前序遍历和中序遍历构造二叉树](build_tree.py)
  - [后序遍历和中序遍历构造二叉树](build_tree.py)
  - [有序数组转换为 BST](build_tree.py)
- 更新
  - [插入节点](bst_operations.py)
  - [删除节点](bst_operations.py)

> 在递归函数有返回值的情况下：如果要搜索一条边，递归函数返回值不为空的时候，立刻返回，如果搜索整个树，直接用一个变量left、right接住返回值，这个left、right后序还有逻辑处理的需要，也就是后序遍历中处理中间节点的逻辑（也是回溯）。
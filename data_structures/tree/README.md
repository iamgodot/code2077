# 树

- [遍历](traversal.py)
  - 前序
    - [翻转二叉树](invert.py)
    - [对称二叉树](is_symmetric.py)
    - [相同的树](is_same.py)
    - [判断子结构](is_substructure.py)
    - [二叉树的合并](merge_trees.py)
    - [二叉树的所有路径](binary_tree_path.py)
    - [路径总和 I/II/III](binary_tree_path.py)
  - 后序
    - [二叉树最大深度](depth.py)
    - [二叉树最小深度](depth.py)
    - [完全二叉树的节点个数](count_node.py) -> 这个是后序吗？二分法如何实现
    - [平衡二叉树](balanced_tree.py)
    - [二叉树的最近公共祖先](lowest_common_ancestor.py)
    - [二叉树的直径长度](diameter.py)
    - [最大路径和](max_path_sum.py)
    - [最长同值路径](longest_univalue_path.py)
    - [二叉树剪枝](prune.py)
  - 层序
    - [填充每个节点的下一个右侧节点指针](populate_next_right_pointers.py)
- BST
  - [BST 的第 k 节点](kth_element.py)
  - [BST 有效性判断](valid_bst.py)
  - [BST 插入节点](bst_operations.py)
  - [BST 删除节点](bst_operations.py)
  - [BST 的恢复](recover_bst.py)
  - [BST 迭代器](bst_iterator.py)
  - [不同的 BST](unique_bst.py)
  - [BST 的中序后继 I/II](inorder_successor.py)
- 结构转换
  - 构造二叉树
    - [前序遍历和中序遍历构造二叉树](build_tree.py)
    - [后序遍历和中序遍历构造二叉树](build_tree.py)
    - [前序遍历和后序遍历构造二叉树](build_tree.py)
  - 转换 BST
    - [有序数组转换为平衡 BST](convert_to_bst.py)
    - [链表转换为 BST](convert_to_bst.py)
    - [验证 BST 的后序遍历](verify.py)
    - [验证 BST 的前序遍历](verify.py)
    - [前序/后序遍历构造 BST](verify.py)
  - 序列化
    - [二叉树](serialization.py)
    - [N 叉树](serialization.py)
    - [BST](serialization.py)
  - [BST 与双向链表](tree_to_doubly_list.py)
- Trie
  - [实现前缀树](trie.py)
  - [添加与搜索单词](words_data_structure.py)
  - [单词搜索 II](algorithms/backtracking/word_search.py)

## 二叉树

满二叉树：如果所有的分支节点都存在左子树和右子树，并且所有叶子节点都在同一层上，则称二叉树为满二叉树。

完全二叉树：如果叶子节点只能出现在最下面两层，并且最下层的叶子节点都依次排列在该层最左边的位置上，具有这种特点的二叉树称为完全二叉树。

二叉搜索树：对于一棵二叉树来说，如果满足任意节点的值都大于该节点左子树所有节点的值，小于该节点右子树所有节点的值，那么这棵树就是二叉搜索树。

平衡二叉搜索树：一种结构平衡的二叉搜索树，叶子节点高度差的绝对值不超过 1，并且左右两个子树都是平衡二叉搜索树。

二叉树的顺序存储结构：

- 使用数组来存储节点，存储位置采用完全二叉树的节点层次编号，从上到下每一层按照从左到右的顺序依次存放二叉树的数据元素。
- 如果某个节点的下标为 i，那么其左孩子节点下标为 `2*i + 1`，右孩子节点下标为 `2*i + 2`。
- 如果某个节点的下标为 i，那么其父节点下标为 `(i-1) // 2`。
- 对于完全二叉树，尤其是满二叉树来说，采用顺序存储可以充分利用存储空间。
- 对于普通二叉树，如果存在很多空节点，采用顺序存储则会浪费很多存储空间。

## 字典树

字典树（Trie），又称为前缀树，是一种字典存储的树形结构。每个节点都包含多个字符的指针，将根节点到某个节点路径上的所有字符连接起来，就是该节点对应的字符串。

字典树的核心思想是空间换时间，利用字符串的公共前缀来降低查询时间，最大限度地减少无谓的字符串比较，以提高查找的效率。

基本性质：

- 根节点不包含字符，其他每个节点包含一个字符。
- 每个节点的子节点都包含不同的字符。
- 每个节点记录是否为某字符串的结尾。

复杂度：

- 时间
  - 构建：O(n) n 为所有字符串长度之和
  - 查询：O(k) k 为查找字符串长度
- 空间：O(d^h) 其中 d 为字符集合大小，h 为树的高度

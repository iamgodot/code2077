# 哈希表

- [字母异位词](valid_anagram.py)
- [赎金信](ransom_note.py)
- [两个数组的交集](intersection.py)
- [快乐数](happy_number.py)
- [两数之和](two_sum.py)
- [四数相加](four_sum_count.py)
- 存在重复元素 I/II
- [有效的字母异位词](valid_anagram.py)
- [两数之和](two_sum.py)
- [字母异位词分组](group_anagrams.py)
- [前 k 个高频元素](algorithms/search/top_k.py)
- [最长连续序列](longest_consecutive_sequence.py)

哈希表本质上是一种基于数组的数据结构，以 key-value 的形式做存储。

从 key -> index 的转换需要借助 hash function 来完成，比如 function = hash(key) % table_size.

使用哈希表的好处是可以在常量时间内完成插入和查询，如 get/put 操作的时间复杂度都是 O(1).

可能碰到的问题是 hash collision，即不同的 key 转换到了同一个 index 上面。针对这个问题的解决方案通常有两种：

1. Seperate Chaining：即每个 index 都对应着一个链表结构，如果发生碰撞的话就增加在链表的最后，查询时也会顺着这条链表进行线性查找。`这种方法在元素过多的情况下性能会下降，因为链表过长会浪费大量的时间。`
2. Open Addressing：在碰撞时继续向后遍历，直到出现一个 empty slot. 根据向后移动步伐大小的不同，有不一样的实现，像 Linear Probing 就是一种最常见的方法，即固定每次挪动一位。`需要注意的是要保证 slots 的数量要大于数据量，另外如果 table 放得太满也会导致性能下降。`

> 一般哈希表都是用来快速判断一个元素是否出现在集合里。

因为使用哈希表需要额外的空间，所以是一种典型的以空间换时间的思路。基于不同的场景，也应当选取恰当的哈希结构：

1. 数组：适合字母的场景，尤其是不考虑大写的情况。好处是只需要固定大小，节省了额外的空间消耗和红黑树等结构的维护成本，速度也会更快。
2. 集合：适合一部分数字的场景，尤其在数组大小受限并且哈希结果分散的情况下，还有个额外好处是可以去重。另外 python 的 collections.Counter 可看作是一种 multiset，对于计数之类的用途来说非常方便。
3. 字典：适合需要存储 <key, value> 结构数据的场景，比如 <数值，下标>. 在 python 中有时 defaultdict 会比 dict 好用很多。

使用中注意：

1. 先判断是否要使用 hash table，依据是场景需不需要快速判断元素的存在，或者是以空间换取时间
2. 选择最适合的数据结构，数组、集合还是字典
3. 确认要存储的数据，如果是字典的话想清楚 key/value 都是什么，key 是否会重复
4. 什么时候向（从）哈希表中添加（删除）数据，什么时候用哈希表做判断

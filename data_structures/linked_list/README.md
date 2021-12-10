# Linked List

相对于数组，链表是另外一种常用的基础数据结构，在内存中分散存储，所以对于插入和删除操作来说效率很高，但是查询会比较慢，这点和数组正好相反。

对单链表来说，节点一般只保存两种数据，存储值和指向下一个节点的指针，而双链表还需要增加额外的指向前一个节点的指针。如果是实现一个链表，还可能需要保存整个链表的长度，便于遍历查找辅助判断。

## 虚拟头部节点

虚拟头是一种常用的链表技巧，可以用来合并删除或插入操作在头部和中部的不同处理。

1. [移除链表元素](remove_elements.py)

## 基础

对于链表的插入和删除的实现，一定要考虑到在头部、中部和尾部的特殊情况。另外，如果参数中的索引超出了链表的长度或者干脆是一个负值，要保证方法返回的是特殊值而不是正常数据。

还有就是对于比较复杂的处理最好先画图模拟好每一步的过程，确认步骤的逻辑之后再进行代码实现，比如经典的反转链表。

1. [链表的基本操作](linked_list.design.py)

2. [反转链表](reverse_list.py)
3. [两两交换节点](swap_pairs.py)

## 双指针

利用快慢双指针技巧可以很好地解决一类链表问题：

1. [删除倒数第N个节点](remove_from_end.py)
2. [链表相交](intersection_node.py)
3. [环形链表](cycle.py)
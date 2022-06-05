class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# 给定二叉树其中的一个结点，请找出其中序遍历顺序的下一个结点并且返回。
# 注意，树中的结点不仅包含左右子结点，而且包含指向父结点的指针。


def find_next(node: TreeNode) -> TreeNode:
    """
    1. 如果右子树存在，那么返回右子树的最小（左）节点
    2. 右子树不存在，向上查找父节点
      1. 如果当前节点为父节点的左子节点，那么直接返回父节点
      2. 如果当前节点为父节点的右子节点，那么继续向上查找
        1. 如果某个父节点为其父节点的左子节点，返回其父节点
        2. 否则最终返回空节点
    """
    if not node:
        return None
    if node.right:
        cur = node.right
        while cur.left:
            cur = cur.left
        return cur
    else:
        cur = node
        while cur.next:
            parent = cur.next
            if cur is parent.left:
                return parent
            else:
                cur = parent
    return None

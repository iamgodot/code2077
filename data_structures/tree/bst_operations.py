# 给定二叉搜索树（BST）的根节点 root 和要插入树中的值 value ，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 输入数据 保证 ，新值和原始二叉搜索树中的任意节点值都不同。
# 注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回 任意有效的结果 。


from typing import Optional

from data_structures.tree import TreeNode


def insert(root: TreeNode, val: int) -> TreeNode:
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)

    return root


# 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。


# 复杂的地方在于，如果删除的节点的左右子树都不为空，需要把左子树挂到右子树的最左子节点下，然后返回右子树
def delete_node(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    if not root:
        return None

    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        if not root.left or not root.right:
            root = root.left or root.right
        else:
            cur = root.right
            while cur.left:
                cur = cur.left
            cur.left = root.left
            root = root.right

    return root

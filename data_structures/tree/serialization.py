from collections import deque

from data_structures.tree import TreeNode, levelorder

# Q: 二叉树的序列化与反序列化

# 层序遍历，比深度遍历更直观一些
# 时间复杂度 O(n)
# 空间复杂度 O(n)


class CodecLevelOrder:
    def serialize(self, root):
        dq = deque([root])
        res = []
        while dq:
            if node := dq.pop():
                res.append(str(node.val))
                dq.appendleft(node.left)
                dq.appendleft(node.right)
            else:
                res.append("X")

        return ",".join(res)

    def deserialize(self, data):
        vals = data.split(",")
        if vals[0] == "X":
            return None
        root = TreeNode(int(vals[0]))
        dq = deque([root])
        i = 1
        while dq:
            node = dq.pop()
            val1, val2 = vals[i], vals[i + 1]
            if val1 != "X":
                node.left = TreeNode(int(val1))
                dq.appendleft(node.left)
            if val2 != "X":
                node.right = TreeNode(int(val2))
                dq.appendleft(node.right)
            i += 2

        return root


# 先序遍历
# 时间复杂度 O(n)
# 空间复杂度 O(n)
class CodecPreOrder:
    def serialize(self, root):
        if not root:
            return "X"

        return (
            str(root.val)
            + ","
            + self.serialize(root.left)
            + ","
            + self.serialize(root.right)
        )

    def deserialize(self, data):
        def _restore(vals) -> TreeNode:
            val = vals.pop(0)
            if val == "X":
                return None
            node = TreeNode(int(val))
            node.left = _restore(vals)
            node.right = _restore(vals)
            return node

        return _restore(data.split(","))


# Q: 二叉搜索树的序列化与反序列化

# 先序遍历
# 时间复杂度 O(n)
# 空间复杂度 O(n)
class CodecPreOrderBST:
    def serialize(self, root) -> str:
        def dfs(node):
            if not node:
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        if not root:
            return ""
        res = []
        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        def _restore(vals, low=-float("inf"), high=float("inf")) -> TreeNode:
            if not vals or vals[0] < low or vals[0] > high:
                return None
            val = vals.pop(0)
            node = TreeNode(val)
            node.left = _restore(vals, low=low, high=val)
            node.right = _restore(vals, low=val, high=high)
            return node

        if not data:
            return None
        return _restore([int(i) for i in data.split(",")])


# Q: N 叉树的序列化与反序列化
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class CodecDfsNT:
    def serialize(self, root: "Node") -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        res = []

        def dfs(root):
            if not root:
                return
            res.append(str(root.val))
            res.append(str(len(root.children)))
            for ch in root.children:
                dfs(ch)

        dfs(root)
        return ",".join(res)

    def deserialize(self, data: str) -> "Node":
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if not data:
            return
        data = iter(data.split(","))

        def dfs():
            root = Node(int(next(data)), [])
            num = int(next(data))
            for _ in range(num):
                child = dfs()
                root.children.append(child)
            return root

        return dfs()


class CodecBfsNT:
    def serialize(self, root: "Node") -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        from collections import deque

        if not root:
            return ""
        queue = deque([root])
        res = []
        while queue:
            node = queue.pop()
            res.append(str(node.val))
            res.append(str(len(node.children)))
            for ch in node.children:
                queue.appendleft(ch)
        return ",".join(res)

    def deserialize(self, data: str) -> "Node":
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        from collections import deque

        if not data:
            return
        data = iter(data.split(","))
        root = Node(int(next(data)), [])  # 注意初始化 children
        queue = deque([[root, int(next(data))]])  # 转换 children num 为 int

        while queue:
            node, num = queue.pop()
            for _ in range(num):
                tmp = int(next(data))
                tmp_num = int(next(data))
                tmp_node = Node(tmp, [])
                node.children.append(tmp_node)
                queue.appendleft([tmp_node, tmp_num])
        return root


if __name__ == "__main__":
    root = TreeNode(
        val=1,
        left=TreeNode(2),
        right=TreeNode(
            3, left=TreeNode(4, left=TreeNode(6), right=TreeNode(7)), right=TreeNode(5)
        ),
    )
    codec = CodecLevelOrder()
    data = codec.serialize(root)
    assert data == "1,2,3,X,X,4,5,6,7,X,X,X,X,X,X"
    node = codec.deserialize(data)
    assert levelorder(root) == [[1], [2, 3], [4, 5], [6, 7]]

    codec = CodecPreOrder()
    data = codec.serialize(root)
    assert data == "1,2,X,X,3,4,6,X,X,7,X,X,5,X,X"
    node = codec.deserialize(data)
    assert levelorder(root) == [[1], [2, 3], [4, 5], [6, 7]]

    root = TreeNode(
        val=3,
        left=TreeNode(2, left=TreeNode(1)),
        right=TreeNode(5, left=TreeNode(4), right=TreeNode(6)),
    )
    codec = CodecPreOrderBST()
    data = codec.serialize(root)
    assert data == "3,2,1,5,4,6"
    node = codec.deserialize(data)
    assert levelorder(root) == [[3], [2, 5], [1, 4, 6]]

from collections import deque

from tree import TreeNode, levelorder

# Q: 二叉树的序列化与反序列化

# 层序遍历，比深度遍历更直观一些
# 时间复杂度 O(n)
# 空间复杂度 O(n)
class CodecLevelOrder:
    def serialize(self, root):
        if not root:
            return ""

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
        if not data:
            return None

        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        dq = deque([root])
        i = 1
        while i < len(vals):
            node = dq.pop()
            val1, val2 = vals[i], vals[i + 1]
            if val1 != "X":
                node.left = TreeNode(val1)
                dq.appendleft(node.left)
            if val2 != "X":
                node.right = TreeNode(val2)
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

        return f"{root.val},{self.serialize(root.left)},{self.serialize(root.right)}"

    def deserialize(self, data):
        def _restore(vals) -> TreeNode:
            val = vals.pop(0)
            if val == "X":
                return None
            node = TreeNode(val)
            node.left = _restore(vals)
            node.right = _restore(vals)
            return node

        return _restore(data.split(","))


# Q: 二叉树的序列化与反序列化
# 先序遍历
# 时间复杂度 O(n)
# 空间复杂度 O(n)
class CodecPreOrderBST:
    def serialize(self, root):
        def _iter(node) -> list:
            if not node:
                return []
            return [node.val] + _iter(node.left) + _iter(node.right)

        return ",".join([str(i) for i in _iter(root)])

    def deserialize(self, data):
        def _restore(vals, lower=-float("inf"), upper=float("inf")) -> TreeNode:
            val = int(vals.pop())
            if val < lower or val > upper:
                return None
            node = TreeNode(val)
            node.left = _restore(vals, upper=val)
            node.right = _restore(vals, lower=val)
            return node

        return _restore(data.split(","))


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

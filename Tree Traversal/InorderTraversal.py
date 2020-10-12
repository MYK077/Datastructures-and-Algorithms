#Left--->root--->right
class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []
        res, stack = [], [root]
        while stack:
            while root:
                stack.append(root.left)
                root = root.left
            node = stack.pop()
            if node:
                res.append(node.val)
                root = node.right
                stack.append(root)                
        return res
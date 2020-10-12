# Root ---> Left ---> Right

class Solution(object):
    def preorderTraversal(self, root):
        res = [] 
        stack = [root]
        
        if not root:
            return None
        
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
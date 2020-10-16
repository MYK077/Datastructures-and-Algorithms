
# from right to left , level by level

from collections import deque
class Solution(object):
    def levelOrder(self,root):
        """
         :type root: TreeNode
         :rtype: List[List[int]]
        """
        if not root:
            return []
        queue, res = deque([root]), []
        
        while queue:
            currLevel = []
            size = len(queue)
            for _ in range(0,size):
                node = queue.popleft()
                if node and node.left:
                    queue.append(node.left)
                if node and node.right:
                    queue.append(node.right)
                currLevel.append(node.val)
            res.append(currLevel)
        return res
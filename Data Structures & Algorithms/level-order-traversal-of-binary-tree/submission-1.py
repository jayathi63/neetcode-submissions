from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        queue = deque([root])
        res = [[root.val]]

        while queue:
            
            c = len(queue)
            val = []

            for i in range(c):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                    val.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    val.append(node.right.val)
            if val:
                res.append(val)

        return res 








        
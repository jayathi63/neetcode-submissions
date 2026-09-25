# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node,min_max):
            minm = min_max[0]
            maxm = min_max[1]
            if not node:
                return True
            
            if node.val <= minm or node.val >= maxm:
                return False
            
            a = dfs(node.left,[minm,node.val])
            b = dfs(node.right,[node.val,maxm])

            return a and b

        return dfs(root,[float("-inf"),float("+inf")])

        


        
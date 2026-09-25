# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def inorder(node,l):
            if not node:
                return
            
            inorder(node.left,l)
            l.append(node.val)
            inorder(node.right,l)

         

        inorder(root,res)
        print(res)
        return res[k-1]
            


        
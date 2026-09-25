# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


        def same_tree(node1,node2):
            # print(node1,node2)
            if not node1 and not node2:
                return True
            
            if not node1 or not node2:
                return False
            
            if node1.val != node2.val:
                return False
            
            a = same_tree(node1.left,node2.left)
            b = same_tree(node1.right,node2.right)

            return a and b

        def dfs(node1,node2):
            
            # print(node1,node2)
            if (not node1 and not node2) or not node2:
                return True
            
            if not node1:
                return False

            a = True
            b = True
            # print(node1.val, node2.val,"dfs")
            if node1.val == node2.val and same_tree(node1,node2):
                return True
            else:
                a = dfs(node1.left,node2)
                b = dfs(node1.right,node2)
            
            return a or b
            

            



        return dfs(root, subRoot)
        
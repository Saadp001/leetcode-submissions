# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        
        if not root:
            return TreeNode(val)

        og_root = root    

        while root:
            
            if root.val > val:
                if root.left:
                    root = root.left
                else:
                    root.left = TreeNode(val)  
                    break

            else:
                if root.right:
                    root = root.right        
                else:
                    root.right = TreeNode(val)
                    break
      

        return og_root          
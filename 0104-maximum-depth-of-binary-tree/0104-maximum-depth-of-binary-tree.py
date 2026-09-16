# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        self.maxi = 1    
        
        def solve(node, cnt):        
            if node is None:
                self.maxi = max(self.maxi, cnt-1)
                return 

            solve(node.left,cnt+1)      
            solve(node.right, cnt+1)

        solve(root,1)
        return self.maxi
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0
        def solve(node, maxi):
            nonlocal cnt
            if not node:
                return 

            solve(node.left, max(node.val,maxi))
            solve(node.right,max(node.val,maxi))
            if node.val >= maxi:
                cnt+=1

                
            

       
        solve(root, root.val)  
        return cnt      
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    ans = []
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:

        ans = []

        def solve(node):
            nonlocal ans

            if not node:
                return

            ans.append(node.val)
            solve(node.left)
            solve(node.right)  

        solve(root)
        ans.sort()
        i = 0
        while i <= len(ans):
            if i == k:
                return ans[i-1]
            else:
                i+=1    

      
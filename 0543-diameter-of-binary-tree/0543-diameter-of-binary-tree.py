# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.di = -1

        def solve(node):
            if not node:
                return 0
            left = solve(node.left)
            right = solve(node.right)

            self.di = max(self.di, left+right)

            return max(left, right) + 1

        solve(root)
        return self.di
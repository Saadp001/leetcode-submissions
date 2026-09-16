class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def solve(node) :
            if not node:
                return 0

            left = solve(node.left)
            right = solve(node.right)

            return 1 + max(left, right)

        return solve(root)
      
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False

        def solve(node, total):
            if not node:
                return False

            total += node.val

            # Check only at a leaf
            if not node.left and not node.right:
                return total == targetSum

            return solve(node.left, total) or solve(node.right, total)

        return solve(root, 0)
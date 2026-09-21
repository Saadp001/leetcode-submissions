class Solution:
    def averageOfSubtree(self, root: TreeNode | None) -> int:

        ans = 0

        def solve(node):
            nonlocal ans

            if not node:
                return 0, 0

            # Get sum and count from left subtree
            left_sum, left_count = solve(node.left)

            # Get sum and count from right subtree
            right_sum, right_count = solve(node.right)

            # Sum of current subtree
            total_sum = node.val + left_sum + right_sum

            # Number of nodes in current subtree
            total_count = 1 + left_count + right_count

            # Check whether current node == subtree average
            if total_sum // total_count == node.val:
                ans += 1

            # Return information needed by parent
            return total_sum, total_count

        solve(root)

        return ans
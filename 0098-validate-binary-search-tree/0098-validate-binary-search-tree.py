class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:

        def solve(node):

            # Empty subtree is valid.
            # For an empty subtree:
            # max = -infinity
            # min = +infinity
            if not node:
                return float('-inf'), float('inf'), True

            # Get information from LEFT subtree
            left_max, left_min, left_flag = solve(node.left)

            # Get information from RIGHT subtree
            right_max, right_min, right_flag = solve(node.right)

            # Current subtree's maximum value
            maxi = max(left_max, node.val, right_max)

            # Current subtree's minimum value
            mini = min(left_min, node.val, right_min)

            # Current subtree is valid only if:
            # 1. Left subtree is valid
            # 2. Right subtree is valid
            # 3. Every value in left subtree < current node
            # 4. Every value in right subtree > current node
            flag = (
                left_flag
                and right_flag
                and left_max < node.val
                and node.val < right_min
            )

            # Give parent the information about our whole subtree
            return maxi, mini, flag

        # solve(root) returns:
        # (maximum, minimum, valid)
        #
        # We only need the third value.
        maxi, mini, flag = solve(root)

        return flag
class Solution:
    def removeLeafNodes(self, root: TreeNode | None, target: int) -> TreeNode | None:

        def solve(node):

            # Nothing to process
            if not node:
                return None

            # First process children
            node.left = solve(node.left)
            node.right = solve(node.right)

            # After deleting children, check if current node
            # has become a leaf and has the target value
            if not node.left and not node.right:
                if node.val == target:
                    return None

            # Keep this node
            return node

        return solve(root)
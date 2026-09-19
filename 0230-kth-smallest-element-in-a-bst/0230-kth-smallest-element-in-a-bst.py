class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:

        ans = []

        def solve(node):
            if not node:
                return

            # Inorder traversal:
            # LEFT → ROOT → RIGHT
            solve(node.left)

            # BST inorder gives values in sorted order
            ans.append(node.val)

            solve(node.right)

        solve(root)

        # k-th smallest is at index k-1
        return ans[k - 1]
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:

        idx = [0]

        def solve(start, end):

            if start > end:
                return None

            # 1. Take root from preorder
            rootval = preorder[idx[0]]
            idx[0] += 1

            root = TreeNode(rootval)

            # 2. Find root in inorder
            i = start
            while inorder[i] != rootval:
                i += 1

            # 3. Build left subtree
            root.left = solve(start, i - 1)

            # 4. Build right subtree
            root.right = solve(i + 1, end)

            return root

        return solve(0, len(inorder) - 1)
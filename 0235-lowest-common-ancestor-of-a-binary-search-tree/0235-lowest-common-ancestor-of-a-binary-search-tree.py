class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode',
                             p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':

        while root:

            # Both p and q are smaller than the current node.
            # Because this is a BST, both nodes MUST be in the left subtree.
            if p.val < root.val and q.val < root.val:
                root = root.left

            # Both p and q are greater than the current node.
            # Therefore, both nodes MUST be in the right subtree.
            elif p.val > root.val and q.val > root.val:
                root = root.right

            # Otherwise, p and q are on different sides of root,
            # OR root itself is p or q.
            #
            # Therefore, current root is their Lowest Common Ancestor.
            else:
                return root
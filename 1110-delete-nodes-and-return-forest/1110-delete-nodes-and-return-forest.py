class Solution:
    def delNodes(self, root: Optional[TreeNode],
                 to_delete: List[int]) -> List[TreeNode]:

        def delete(node, s, res):

            # Reached an empty node
            if not node:
                return None

            # First process the left subtree
            # The recursive call may delete something,
            # so we reconnect the updated subtree to node.left.
            node.left = delete(node.left, s, res)

            # Then process the right subtree
            # Again, reconnect the updated subtree.
            node.right = delete(node.right, s, res)

            # Now check whether the CURRENT node should be deleted
            if node.val in s:

                # If current node is deleted,
                # its surviving left child becomes a new tree root.
                if node.left:
                    res.append(node.left)

                # Its surviving right child also becomes
                # a new tree root.
                if node.right:
                    res.append(node.right)

                # Return None so the parent disconnects this node.
                return None

            # Current node is not deleted,
            # so return it to its parent.
            return node

        # Set gives O(1) average lookup for:
        # "Should this node be deleted?"
        s = set(to_delete)

        # This will store the roots of all resulting trees.
        res = []

        # IMPORTANT:
        # delete() can change the original root.
        # For example, if root itself is deleted,
        # this will become None.
        root = delete(root, s, res)

        # If the original root survived,
        # it is also one of the forest roots.
        if root:
            res.append(root)

        return res
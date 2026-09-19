class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:

        # We reached an empty position.
        # This means the key does not exist in this subtree.
        if not root:
            return root

        # key is smaller than current node.
        # Because this is a BST, key can only exist in the LEFT subtree.
        #
        # After deletion, the left subtree might have changed,
        # so we reconnect the returned subtree to root.left.
        if root.val > key:
            root.left = self.deleteNode(root.left, key)

        # key is larger than current node.
        # Therefore, key can only exist in the RIGHT subtree.
        #
        # Again, the recursive call returns the UPDATED right subtree,
        # so we reconnect it to root.right.
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        # root.val == key
        # We have FOUND the node that needs to be deleted.
        else:

            # CASE 1:
            # No left child.
            #
            # The node has either:
            #   - no children, OR
            #   - only a right child
            #
            # So simply replace this node with its right subtree.
            if not root.left:
                return root.right

            # CASE 2:
            # No right child.
            #
            # The node has only a left child.
            # Replace this node with its left subtree.
            elif not root.right:
                return root.left

            # CASE 3:
            # The node has BOTH left and right children.
            #
            # We cannot simply remove it because we need to
            # maintain the BST property.
            #
            # Find the inorder successor:
            # → smallest value in the RIGHT subtree.
            cur = root.right

            # Keep going left because the leftmost node
            # is the smallest node in this subtree.
            while cur.left:
                cur = cur.left

            # Copy the successor's value into the current node.
            #
            # We are NOT physically moving the successor yet.
            # We are replacing the value of the node we wanted to delete.
            root.val = cur.val

            # Now there are TWO copies of cur.val:
            #
            #       root
            #         ↓
            #      cur.val
            #
            # and the original successor further down.
            #
            # So delete the ORIGINAL successor from the right subtree.
            root.right = self.deleteNode(root.right, cur.val)

        # Return the current (possibly modified) subtree.
        #
        # This is important because the parent needs the UPDATED subtree
        # after the recursive deletion.
        return root
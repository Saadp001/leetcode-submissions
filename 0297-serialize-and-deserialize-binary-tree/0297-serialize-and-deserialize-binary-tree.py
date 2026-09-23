# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        # We will store the tree as:
        # ROOT -> LEFT -> RIGHT
        # '#' represents a None node
        values = []

        def solve(node):

            # If there is no node, store '#'
            if not node:
                values.append("#")
                return

            # Store the current node's value
            values.append(str(node.val))

            # Recursively store left and right
            solve(node.left)
            solve(node.right)

        solve(root)

        # Convert the list into one string
        return ",".join(values)


    def deserialize(self, data):

        # Convert the string back into individual values
        # "1,2,#,#,3,#,#"
        #       ↓
        # ["1", "2", "#", "#", "3", "#", "#"]
        data = data.split(",")

        # This keeps track of which value we are currently reading
        idx = 0

        def solve():
            nonlocal idx

            # Current value is '#'
            # → this position in the tree is empty
            if data[idx] == "#":
                idx += 1
                return None

            # Create the current node
            node = TreeNode(int(data[idx]))

            # Move to the next value
            idx += 1

            # The serialization order was:
            # ROOT -> LEFT -> RIGHT
            #
            # So we reconstruct in the same order.
            node.left = solve()
            node.right = solve()

            # Return the completed subtree
            return node

        # Start rebuilding from the first value
        return solve()
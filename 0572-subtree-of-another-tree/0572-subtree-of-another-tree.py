# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:

        def same(node, subnode):


                if not node and not subnode:
                    return True

                if not node or not subnode:
                    return False

                if node.val != subnode.val:
                    return False    

                left = same(node.left, subnode.left)
                right = same(node.right, subnode.right)

                return left and right

        def solve(node):
            if not node:
                return False

            if same(node, subRoot):
                return True

            return solve(node.left) or solve(node.right)        

        return solve(root)
        
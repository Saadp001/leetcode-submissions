# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root :
            return []

        res = []
        q = collections.deque()
        q.append(root)

        while q:
            q_len = len(q)
            lvl = []

            for _ in range(q_len):
                node = q.popleft()  # node holds the object which have it's own val , left and right

                if node:
                    lvl.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if lvl:
                res.append(lvl)

        return res

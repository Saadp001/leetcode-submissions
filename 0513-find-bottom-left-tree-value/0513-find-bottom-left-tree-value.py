# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode | None) -> int:
        if not root:
            return -1

        q = deque([root])
        res = []
        while q:
            lvl = []
            l_lvl = len(q)
            
            for _ in range(l_lvl):
                node = q.popleft()
                lvl.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        if lvl:
            res.append(lvl)  

        return res[-1][0]     

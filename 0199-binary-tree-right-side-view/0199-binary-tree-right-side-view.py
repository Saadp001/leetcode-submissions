# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            ans= []
            len_q = len(q)

            for _ in range(len_q):
                node = q.popleft()
                ans.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)  
        
            res.append(ans)
        sol = []   
        for i in range(len(res)):
            sol.append(res[i][-1])

        return sol    
             
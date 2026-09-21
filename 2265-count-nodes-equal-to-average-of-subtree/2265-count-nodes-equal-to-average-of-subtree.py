# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0
        def solve(node):
            nonlocal ans

            if not node:
                return 0,0

            left_sum , left_cnt = solve(node.left)
            right_sum, right_cnt = solve(node.right)


            total_sum = left_sum + right_sum + node.val
            total_cnt = left_cnt + right_cnt + 1

            if total_sum // total_cnt == node.val:
                ans+=1

            return total_sum, total_cnt  


        solve(root)
        return ans
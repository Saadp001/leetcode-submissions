class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        m = nums[0]
        for i in nums:
            if i > m:
                m = i
        ans = 0
        for i in range(0, k):
            ans += m
            m += 1
        return ans
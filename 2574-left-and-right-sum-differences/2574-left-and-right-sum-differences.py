class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        l = []
        total = 0
        for i in range(len(nums)):            
            l.append(total)
            total += nums[i]
      
        r = [0] * len(nums)
        rtotal = 0
        for i in range(len(nums)-1, -1, -1):            
            r[i] = rtotal
            rtotal += nums[i]

        ans = []
        while i < len(nums):
            ans.append(abs(l[i]-r[i]))
            i+=1

        return ans    
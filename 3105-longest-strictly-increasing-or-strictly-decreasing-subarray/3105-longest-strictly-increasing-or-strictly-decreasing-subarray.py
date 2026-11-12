class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if max(nums) == min(nums):
            return 1
        res = -1
        
        n = len(nums)
        def inc():
            nonlocal res
            l,r = 0,0
            while r<n-1:
                if nums[r] < nums[r+1]:
                    r+=1
                    res = max(res, r-l+1)
                else: 
                    r+=1
                    l = r

        def dec():
            nonlocal res
            l,r = 0,0
            while r<n-1:
                if nums[r] > nums[r+1]:
                    r+=1
                    res = max(res, r-l+1)
                else:
                    r+=1
                    l = r
        inc()
        dec()
        return res            
                    

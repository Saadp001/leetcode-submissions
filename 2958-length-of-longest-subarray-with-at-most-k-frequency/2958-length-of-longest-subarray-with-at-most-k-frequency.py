class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        hm = {}
        best = 1
        l = 0 
        r = 0
        while r < len(nums):
            hm[nums[r]] = hm.get(nums[r],0) +1    
            
            while hm[nums[r]] > k:             
                hm[nums[l]] = hm.get(nums[l],0) -1
                l+=1
           
            best = max(best, r-l+1)  
            r+=1    
        return best        

            

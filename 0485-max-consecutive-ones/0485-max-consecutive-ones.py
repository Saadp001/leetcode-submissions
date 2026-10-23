class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        r = 0
        maxi = -1
        cnt = 0
        while r < len(nums): 
            if nums[r]==1:
                cnt+=1
                r+=1
            else:
                
                cnt = 0
                r+=1
            maxi = max(cnt, maxi)    

        return maxi        

          
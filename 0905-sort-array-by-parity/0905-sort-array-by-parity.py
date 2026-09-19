class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        i = 0
        
        while i < n:
            
            if nums[i] %2 != 0 :
                j = i+1

                while j < n and nums[j] % 2 !=0:
                    j+=1
                if j < n:    
                    nums[i], nums[j] = nums[j] , nums[i]   
            i+=1 
        return nums       


       
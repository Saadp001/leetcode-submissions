class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            total = 0
            j = 0
            val = str(nums[i])
            while j < len(val):
                total+= int(val[j])    
                j+=1
            if total == i:
                return i
                break

        return -1            

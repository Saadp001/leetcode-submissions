class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        total = 0

        for i, val in enumerate(nums, start = 1):   
            if len(nums)%i ==0:
                total+=val*val

        return total        
         
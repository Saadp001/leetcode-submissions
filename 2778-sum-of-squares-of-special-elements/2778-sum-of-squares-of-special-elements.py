class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        l = []
        total = 0
        for i, val in enumerate(nums):
            l.append((i+1, val))

        for i, val in l:
            if len(nums)%i ==0:
                total+=val*val

        return total        
         
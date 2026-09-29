class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        maxi = -1
        maxi_idx = -1
        for i in range(len(nums)):
            if nums[i] > maxi:
                maxi = nums[i]
                maxi_idx = i


        for num in nums:
            if num != maxi and num*2 > maxi:
                return -1    
        return maxi_idx       
        
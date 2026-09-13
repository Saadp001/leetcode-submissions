class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = -1
        smaxi = -1

        for i in range(len(nums)):
            if nums[i] > maxi:
                smaxi = maxi
                maxi = nums[i]

            elif nums[i] > smaxi :
                smaxi =nums[i]    

        return (maxi-1) * (smaxi-1)        


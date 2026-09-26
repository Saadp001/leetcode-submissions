class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        nums = heights.copy()
        cnt = 0
        for i in range(len(nums)):
            for j in range(0, len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                   

        for i in range(len(nums)):
            if nums[i] != heights[i]:
                cnt+=1

        return cnt                     


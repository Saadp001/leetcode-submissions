class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        nums = intervals
        res = []
        for i in range(len(nums)):
            for j in range( len(nums)):
                if i != j and nums[i][0] >= nums[j][0] and nums[i][1] <= nums[j][1]:
                    res.append(nums[i])
                    break
        return len(nums) - len(res)        
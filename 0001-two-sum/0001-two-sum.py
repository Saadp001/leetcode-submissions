class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hm = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hm:
                return [i, hm[comp]]

            hm[nums[i]] = i

        return [-1,-1]    
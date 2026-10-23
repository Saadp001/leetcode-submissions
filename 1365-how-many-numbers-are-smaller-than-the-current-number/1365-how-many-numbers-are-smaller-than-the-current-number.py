class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        ans = [0]*len(nums)

        for i in range(len(nums)):
            cnt = 0
            for j in range(len(nums)):
                if nums[i] > nums[j] and i != j:
                    cnt+=1
            ans[i] = cnt

        return ans    
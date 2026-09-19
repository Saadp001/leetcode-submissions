class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * n

        i = 0
        for num in nums:
            if num % 2 == 0:
                ans[i] = num
                i += 2

        j = 1
        for num in nums:
            if num % 2 != 0:
                ans[j] = num
                j += 2

        return ans
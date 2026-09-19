class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        ans = []

        for num in nums:
            if num % 2 == 0:
                ans.append(num)

        for num in nums:
            if num % 2 != 0:
                ans.append(num)

        return ans                 
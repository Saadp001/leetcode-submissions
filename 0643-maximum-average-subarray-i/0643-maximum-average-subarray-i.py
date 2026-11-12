
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        l = 0
        r = 0
        maxi = float('-inf')
        total = 0

        while r < len(nums):
            total += nums[r]

            if r - l + 1 == k:
                maxi = max(maxi, total / k)
                total -= nums[l]
                l += 1

            r += 1

        return maxi

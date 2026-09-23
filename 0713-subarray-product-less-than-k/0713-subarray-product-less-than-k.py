class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:

        if k <= 1:
            return 0

        ans = 0
        l = 0
        total = 1

        for r in range(len(nums)):
            total *= nums[r]

            while total >= k:
                total //= nums[l]
                l += 1

            ans += r - l + 1

        return ans
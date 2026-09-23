class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        l = 0
        r = 0
        total = sum(nums) - x
        maxi = 0
        lon = 0

        while r < len(nums):
            lon += nums[r]
            r += 1

            while lon > total and l < r:
                lon -= nums[l]
                l += 1

            if lon == total:
                maxi = max(maxi, r - l)

        if maxi == 0 and total != 0:
            return -1

        return len(nums) - maxi

class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left, right = 0, max(diff)

        while left < right:
            mid = (left + right) // 2
            ops = sum(max(0, d - mid) for d in diff)

            if ops <= k:
                right = mid
            else:
                left = mid + 1

        limit = left
        ans = 0
        remaining = k

        for d in diff:
            reduction = max(0, d - limit)
            remaining -= reduction
            ans += min(d, limit) ** 2

        # Use any leftover operations to reduce differences
        # currently equal to limit by one.
        if limit > 0:
            ans -= max(0, remaining) * (2 * limit - 1)

        return ans

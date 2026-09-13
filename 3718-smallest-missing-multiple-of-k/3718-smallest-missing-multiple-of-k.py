class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s = set(nums)
        i = k
        while True:
            if i not in s:
                return i
                break

            i += k

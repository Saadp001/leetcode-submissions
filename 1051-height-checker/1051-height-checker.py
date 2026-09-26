class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        count = [0] * 101

        for h in heights:
            count[h] += 1

        ans = 0
        expected = 0

        for i in range(len(heights)):
            while count[expected] == 0:
                expected += 1

            if heights[i] != expected:
                ans += 1

            count[expected] -= 1

        return ans
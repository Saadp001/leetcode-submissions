class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        expected = sorted(heights)
        i = 0
        j = 0
        cnt = 0
        while i < len(expected):
            if heights[j] != expected[i]:
                cnt+=1
            i+=1
            j+=1

        return cnt        
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        maxi = -1

        for i in range(len(colors)):
            for j in range(len(colors)):
                if colors[i] != colors[j]:
                    maxi = max(maxi, abs(i-j))

        return maxi        
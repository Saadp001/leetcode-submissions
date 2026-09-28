class Solution:
    def maxDepth(self, s: str) -> int:
        maxi = 0
        cnt = 0
        for char in s:
            if char == '(':
                cnt +=1

                maxi = max(cnt, maxi)

            elif char == ")":
                cnt -=1

        return maxi            
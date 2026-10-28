class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        nums = temperatures
        n = len(nums)

        stack = []
        ans = [0]*n
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                prev = stack.pop()

                ans[prev] = i - prev
            stack.append(i)

        return ans    
     
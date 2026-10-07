class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []

        def solve(arr, visited):
            if len(arr) == len(nums):
                ans.append(arr[:])
                return 
 
            for i in range(len(nums)):
                if i not in visited:
                    arr.append(nums[i])
                    visited.add(i)

                    solve(arr, visited) 
                    arr.pop()
                    visited.remove(i)
            

        solve([], set()) 
        return ans                   
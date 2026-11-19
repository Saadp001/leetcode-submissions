class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def solve(i):
            if i == 1 or i ==0:
                return 1


            if i not in memo: # if absent, first put it and return it at last
                memo[i] = solve(i-1) + solve(i-2)
            # and if present directly return 
            return memo[i]    

        return solve(n)

            # so if cond will check and if not present put and return and if present then if not valid directly return 
            # in both the cases return memo[i]
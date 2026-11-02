class Solution:
    def fib(self, n: int) -> int:
        memo = [-1] * (n + 1)   # -1 means "not computed yet"

        def solve(i):
            if i <= 1:               # base cases: fib(0)=0, fib(1)=1
                return i

            if memo[i] != -1:        # 1. already computed? return it
                return memo[i]

            memo[i] = solve(i - 1) + solve(i - 2)   # 2. compute, 3. store
            return memo[i]

        return solve(n)
        
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # is_pal[i][j] = True if s[i..j] is a palindrome
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True

        # minLen[i] = length of the shortest valid (>=k) palindrome starting at i, or 0 if none
        minLen = [0] * n
        for i in range(n):
            for j in range(i + k - 1, n):
                if is_pal[i][j]:
                    minLen[i] = j - i + 1
                    break

        # dp[i] = max non-overlapping palindromes achievable using s[i:]
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1]                    # skip index i
            if minLen[i]:
                dp[i] = max(dp[i], 1 + dp[i + minLen[i]])   # take shortest palindrome at i

        return dp[0]
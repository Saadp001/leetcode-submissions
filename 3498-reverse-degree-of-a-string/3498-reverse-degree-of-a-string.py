class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for char in range(len(s)):
            val = 26 - (ord(s[char]) - ord('a'))
            total += val*(char+1)
        return total    
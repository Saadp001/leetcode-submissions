class Solution:
    def countPrefixes(self, words: list[str], s: str) -> int:
        ans = 0
        for word in words:
            if len(word) <= len(s):
                if s[:len(word)] == word:
                    ans+=1

        return ans            
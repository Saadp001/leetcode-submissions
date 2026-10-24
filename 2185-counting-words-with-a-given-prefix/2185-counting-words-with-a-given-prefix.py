class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        ans = 0
        for word in words:
            char = ""
            for c in word:
                char+=c
                if char == pref:
                    ans+=1

        return ans            
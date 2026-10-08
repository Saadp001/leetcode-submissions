class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depth = 0
        ans = ""

        for ch in s:
            if ch == "(":
                depth += 1
                if depth > 1:
                    ans += ch
            else:
                if depth > 1:
                    ans += ch
                depth -= 1

        return ans
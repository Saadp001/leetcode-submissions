
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hm = {}
        i = 0

        for p in pattern:
            char = ""

            while i < len(s):
                if s[i] == " ":
                    i += 1
                    break

                char += s[i]
                i += 1

            # Missing word
            if char == "":
                return False

            if p not in hm:
                # Different characters cannot map to the same word
                if char in hm.values():
                    return False
                hm[p] = char

            # Same character must map to the same word
            elif hm[p] != char:
                return False

        # Extra words remaining in s
        if i < len(s):
            return False

        return True

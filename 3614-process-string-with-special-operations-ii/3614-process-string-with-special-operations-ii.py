class Solution:
    def processStr(self, s: str, k: int) -> str:

        # Store the length after every operation
        lengths = [0]

        for ch in s:
            length = lengths[-1]

            if ch.isalpha():
                length += 1

            elif ch == '*':
                if length > 0:
                    length -= 1

            elif ch == '#':
                length *= 2

            elif ch == '%':
                pass   # length doesn't change

            lengths.append(length)

        if k >= lengths[-1]:
            return "."

        # Work backwards
        for i in range(len(s) - 1, -1, -1):

            ch = s[i]
            old_len = lengths[i]
            new_len = lengths[i + 1]

            if ch.isalpha():
                # This operation added one character.
                # If k points to this newly added character:
                if k == old_len:
                    return ch

            elif ch == '*':
                # Deleted last character.
                pass

            elif ch == '#':
                # abc -> abcabc
                k = k % old_len

            elif ch == '%':
                # abc -> cba
                k = new_len - 1 - k

        return "."
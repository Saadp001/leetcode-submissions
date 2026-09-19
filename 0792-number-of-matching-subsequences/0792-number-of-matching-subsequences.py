from bisect import bisect_right

class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:

        pos = {}

        for i, ch in enumerate(s):
            if ch not in pos:
                pos[ch] = []
            pos[ch].append(i)

        def subs(word):
            prev = -1

            for ch in word:
                if ch not in pos:
                    return False

                arr = pos[ch]

                # first position > prev
                idx = bisect_right(arr, prev)

                if idx == len(arr):
                    return False

                prev = arr[idx]

            return True

        cnt = 0

        for word in words:
            if subs(word):
                cnt += 1

        return cnt
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        h = []
        for char, freq in count.items():
            heapq.heappush(h, (-freq, char))

        res = ""
        prev_freq, prev_char = 0, ""

        while h:
            freq, char = heapq.heappop(h)
            res += char

            # push previous char back if it still has count remaining
            if prev_freq < 0:
                heapq.heappush(h, (prev_freq, prev_char))

            # current becomes previous for next round
            prev_freq = freq + 1  # freq is negative, +1 means one less count
            prev_char = char

        return res if len(res) == len(s) else ""
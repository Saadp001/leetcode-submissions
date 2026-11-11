class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        hm = Counter(arr)
        s = set()
        for freq in hm.values():
            s.add(freq)

        return len(s) == len(hm)

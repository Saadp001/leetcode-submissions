class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hm = Counter(nums)
        h  = []
        for num, freq in hm.items():
            heapq.heappush(h, (freq, num))

            if len(h) > k:
                heapq.heappop(h)

        ans = []
        while h:
            freq, num = heapq.heappop(h)
            ans.append(num)

        return ans    
             


            
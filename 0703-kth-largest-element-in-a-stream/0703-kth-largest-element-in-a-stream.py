class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = []
        for n in nums:
            heapq.heappush(self.heap, n)

        if len(self.heap) > k:
            heapq.heappop((self.heap))   

    def add(self, val: int) -> int:
        res = []
        heapq.heappush(self.heap, val)
        
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
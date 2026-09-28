class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        res = []
        h = []
        heapq.heapify(h)
        for i in range(len(points)):
            dis = points[i][0]**2 + points[i][1]**2

            heapq.heappush(h,(dis, points[i]))

        for _ in range(k):
            dis, p = heapq.heappop(h)
            res.append(p)

        return res      

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:

        hts = grid
        m = len(hts)
        n = len(hts[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        dist = [[0]* n for _ in range(m)]

        n_health = health - hts[0][0]

        if n_health <= 0:
            return False

        dist[0][0] = n_health

        h = [[ -(n_health), (0,0)]]

        while h :
            neg_health, (i,j) = heapq.heappop(h)
            curr_health = - neg_health

            if curr_health > dist[i][j]:
                continue

            if i == m-1 and j == n-1 :
                return True

            for di, dj in directions:
                ni = i + di
                nj = j + dj
            
                if 0 <= ni < m and 0 <= nj < n:
                    new_health = curr_health - hts[ni][nj]

                    if new_health >= 1 and new_health > dist[ni][nj]:
                        dist[ni][nj] = new_health
                        heapq.heappush(h, (-new_health, (ni,nj)))

        return False        

                 
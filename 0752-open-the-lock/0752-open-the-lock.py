class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        dead = set(deadends)

        if '0000' in dead:
            return -1

        level = 0

        q = deque(['0000'])
        visited = {'0000'}

        while q:
            len_q = len(q)

            for _ in range(len_q):
                curr = q.popleft()

                if curr in dead:
                    continue

                if curr == target:
                    return level

                for i in range(4):
                    digit = int(curr[i])        

                    for move in [-1,1]:
                        new_digit = (digit + move) % 10
                        
                        nxt = curr[:i] + str(new_digit) + curr[i+1:]

                        if nxt not in dead and nxt not in visited:
                            visited.add(nxt)

                            q.append(nxt)

            level +=1

        return -1                    
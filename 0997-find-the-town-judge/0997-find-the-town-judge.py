class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        incoming = {}
        outgoing = {}
 
        for i, j in trust:
            incoming[j] = incoming.get(j, 0)+1
            outgoing[i] = outgoing.get(i, 0)+1

        for i in range(1, n+1):
            if incoming.get(i, 0) == n-1 and outgoing.get(i,0) == 0:
                return i

        return -1        
 
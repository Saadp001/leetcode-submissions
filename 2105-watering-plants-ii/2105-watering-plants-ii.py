class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        N = len(plants)
        i, j = 0, N -1
        
        if N == 1: 
            return 0
        
        totalFills = 0
        aliceCan, bobCan = capacityA, capacityB
        
        while i <= j:
            
            if i == j:
                if aliceCan >= bobCan:
                    if aliceCan < plants[i]:
                        totalFills += 1
                    i += 1
    
                else:
                    if bobCan < plants[j]:
                        totalFills += 1
                    j -= 1 
            
            else:
                if aliceCan < plants[i]:
                    aliceCan = capacityA
                    totalFills += 1
                
                aliceCan -= plants[i]
                i += 1
                
                if bobCan < plants[j]:
                    bobCan = capacityB;
                    totalFills += 1
                
                bobCan -= plants[j]
                j -= 1
            
        return totalFills
        
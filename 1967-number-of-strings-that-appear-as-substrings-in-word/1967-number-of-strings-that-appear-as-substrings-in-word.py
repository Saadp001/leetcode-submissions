class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        s = set()
        for i in range(len(word)):
            for j in range(i+1,len(word)+1):
                
                s.add(word[i:j])
        cnt = 0
        for p in patterns:
            if p in s:
                cnt+=1

        return cnt        
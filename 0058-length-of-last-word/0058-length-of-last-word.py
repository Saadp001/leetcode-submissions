class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cnt = 0
        s = s.strip()
        for i in range(len(s)-1, -1, -1):
            
            if s[i] == ' ':
                break
            cnt +=1
        return cnt 
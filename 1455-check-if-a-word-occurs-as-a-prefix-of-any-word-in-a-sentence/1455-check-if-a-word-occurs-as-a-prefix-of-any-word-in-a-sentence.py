class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        cnt = 1
        char = ""
        for s in sentence:
            if s == ' ':
                cnt+=1
                char = ""
            else:    
                char+=s
                if char == searchWord:
                    return cnt
        return -1            

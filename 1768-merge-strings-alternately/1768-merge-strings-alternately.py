class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        st = ""
        l1 = len(word1)
        l2 = len(word2)
        i = 0
        j = 0
        while i < l1 and j < l2:
            st+=word1[i]
            i+=1
            st+=word2[j]
            j+=1
        while i < l1 and j == l2:
            st+=word1[i]
            i+=1     
        while j < l2 and i == l1:
            st+= word2[j]    
            j+=1
        return st    
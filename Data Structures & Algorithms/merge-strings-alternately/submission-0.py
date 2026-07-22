class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j=0,0
        new_string=[]
        while i < len(word1) and j < len(word2):
            new_string.append(word1[i])
            new_string.append(word2[j])
            i+=1
            j+=1
        new_string.append(word1[i:])
        new_string.append(word2[j:])
        return "".join(new_string)
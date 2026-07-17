class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r,l=len(s)-1, 0 # we traval the string in reverse order  
        while s[r]== " ": # check if space at the starting point 
            r-=1   # if there is space at start than lower the i  
        while r>=0 and s[r] != " ": # if the char not sapce  and it is char 
            l+=1 # incremant the l by one 
            r-=1 #lower the r for cover the string
        return l
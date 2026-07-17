class Solution:
    def scoreOfString(self, s: str) -> int:
        l=0
        r=1
        score=0
        while r< len(s): # true wile r is less than the len of string
            diff=abs(ord(s[l]) - ord(s[r])) #it calculate the absolute diif of ascll value 
            score+=diff #it store the diffrence and addthem with previus diff
            l+=1
            r+=1
        return score
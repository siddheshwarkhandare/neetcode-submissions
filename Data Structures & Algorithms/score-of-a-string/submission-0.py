class Solution:
    def scoreOfString(self, s: str) -> int:
        l=0
        r=1
        score=0
        while r< len(s):
            diff=abs(ord(s[l]) - ord(s[r]))
            score+=diff
            l+=1
            r+=1
        return score
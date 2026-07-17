class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sy=s.strip()
        for i,n in enumerate(sy[::-1]):
            if n== " ":
                return i
                break
        return len(sy)
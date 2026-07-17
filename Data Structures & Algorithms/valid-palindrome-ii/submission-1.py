class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            a = s[:i] + s[i+1:]
            if len(a)%2 == 1:
                second = len(a)//2+1
            else:
                second = len(a)//2
            if a[:len(a)//2] == a[second:][::-1]:
                return True
        return False

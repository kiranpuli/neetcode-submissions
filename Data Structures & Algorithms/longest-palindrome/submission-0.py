class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = Counter(s)
        rem = 0
        res = 0
        for k, f in d.items():
            if f&1==0:
                res+=f
            else:
                res+=f-1
                rem = 1
        
        return res+rem
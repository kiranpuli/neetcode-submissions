class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        n = len(s)
        a = s
        b = s[::-1]
        res=-1
        for i in range(n):
            key = a[i]

            l = i
            idx = b.find(key)
            r = n-idx-1
            res=max(res, r-l-1)
        
        return res
        
        
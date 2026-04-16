class Solution:
    def mergeAlternately(self, a: str, b: str) -> str:
        res = ""
        i = j = 0
        while i<len(a) or j<len(b):
            if i<len(a):
                res+=a[i]
            if j<len(b):
                res+=b[j]
            i+=1
            j+=1
        return res

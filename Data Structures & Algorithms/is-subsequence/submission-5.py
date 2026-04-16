class Solution:
    def isSubsequence(self, a: str, b: str) -> bool:
        i = j = 0
        m, n = len(a), len(b)

        while i<m and j<n:
            if a[i]==b[j]:
                i+=1
            j+=1
        
        return i==m
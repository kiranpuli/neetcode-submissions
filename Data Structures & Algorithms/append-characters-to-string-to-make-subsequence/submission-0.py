class Solution:
    def appendCharacters(self, a: str, b: str) -> int:
        i = j = 0
        m, n = len(a), len(b)

        while i<m and j<n:
            if a[i]==b[j]:
                j+=1
            i+=1

        return n-j
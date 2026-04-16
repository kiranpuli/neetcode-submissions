class Solution:
    def isSubsequence(self, a: str, b: str) -> bool:
        # base 
        if not a:
            return True

        i = 0
        for j in range(len(b)):
            if a[i]==b[j]:
                i+=1
            if i==len(a):
                return True
        
        return False
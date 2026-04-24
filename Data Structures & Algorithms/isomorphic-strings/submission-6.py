class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        rev_d = {}

        for a,b in zip(s, t):
            if a not in d and b not in rev_d:
                d[a]=b
                rev_d[b]=a
            else:
                if a in d and d[a]!=b:
                    return False
                elif b in rev_d and rev_d[b]!=a:
                    return False
        
        return True
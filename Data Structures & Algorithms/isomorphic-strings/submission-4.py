class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = dict()
        rev_d = dict()

        for i, j in zip(s, t):
            if i not in d:
                if j not in rev_d:
                    d[i]=j
                    rev_d[j]=i
                else:
                    if i!=rev_d[j]:
                        return False                
            else:
                if d[i]!=j:
                    return False
        return True

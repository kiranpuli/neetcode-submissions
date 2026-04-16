class Solution:
    def isAnagram(self, a: str, b: str) -> bool:
        d1, d2 = Counter(a), Counter(b)

        for k in d1.keys():
            if k not in d2 or d2[k]!=d1[k]:
                return False
        
        for k in d2.keys():
            if k not in d1 or d2[k]!=d1[k]:
                return False

        return True
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        req = Counter(ransomNote)
        avail = Counter(magazine)

        for k, f in req.items():
            if k not in avail:
                return False
            else:
                if avail[k]<f:
                    return False
        
        return True

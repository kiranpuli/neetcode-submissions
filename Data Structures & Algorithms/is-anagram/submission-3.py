class Solution:
    def isAnagram(self, A: str, B: str) -> bool:
        da = Counter(A)
        db = Counter(B)

        for k,v in da.items():
            if k not in db.keys() or v!=db[k]:
                return False

        if len(set(db.keys())-set(da.keys()))>0:
            return False

        return True
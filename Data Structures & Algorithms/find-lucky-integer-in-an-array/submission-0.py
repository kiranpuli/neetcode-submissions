from math import inf

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = Counter(arr)
        res = -1

        for k,v in d.items():
            if k==v:
                res = max(res, k)
        return res
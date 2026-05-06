from collections import defaultdict

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        d = defaultdict(int)
        n = len(grid)
        for nums in grid:
            for k in nums:
                d[k]+=1

        res = [0, 0]
        for k in range(1, (n*n)+1):
            if k not in d.keys():
                res[1]=k
            else:
                if d[k]>1:
                    res[0]=k
        return res


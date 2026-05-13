from math import comb

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        

        d = Counter(nums)
        res = 0
        for k,v in d.items():
            res+=comb(v, 2)
        
        return res
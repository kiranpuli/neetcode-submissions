class Solution:
    def maxDifference(self, s: str) -> int:
        d = Counter(s)
        ma = 0
        mi = 10**9
        for k, f in d.items():
            if f&1:
                ma = max(ma, f)
            else:
                mi = min(mi, f)
        
        return ma-mi
            
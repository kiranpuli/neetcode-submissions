class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        mi = prices[0]

        for i in prices:
            res = max(res, i-mi)
            if i<mi:
                mi=i
        
        return res

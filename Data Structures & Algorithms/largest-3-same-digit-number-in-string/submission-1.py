class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        w=3
        for i in range(9, -1, -1):
            good = str(i)*w
            if good in num:
                return good
        return ""
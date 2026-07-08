class Solution:
    def minOperations(self, s: str) -> int:
        
        n = len(s)
        
        def solve(s, start):
            res = 0
            nums = [int(i) for i in s]
            pre = start
            for i in range(n):
                if nums[i]==pre:
                    nums[i]^=1
                    res+=1
                pre=nums[i]
            return res
        
        return min(solve(s, 0), solve(s, 1))



        
            
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        l = r = 0

        while r<n:
            while r<n and nums[r]==1:
                res = max(res, r-l+1)
                r+=1
            r+=1
            l=r
        
        return res
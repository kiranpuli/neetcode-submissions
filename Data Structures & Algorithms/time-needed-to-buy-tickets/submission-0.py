from collections import deque

class Solution:
    def timeRequiredToBuy(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            if i<=k:
                res+=min(nums[i], nums[k])
            else:
                res+=min(nums[i], nums[k]-1)
        return res
       


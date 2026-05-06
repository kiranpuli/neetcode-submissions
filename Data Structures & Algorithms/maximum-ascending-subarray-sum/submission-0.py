class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        res = inc = nums[0]
        n = len(nums)
        for i in range(1, n):
            if nums[i]>nums[i-1]:
                inc+=nums[i]
            else:
                inc=nums[i]
            
            res = max(res, inc)
        
        return res


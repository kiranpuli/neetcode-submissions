class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        n = len(nums)
        res = inc = dec = 1
        for i in range(n-1):
            if nums[i]<nums[i+1]:
                inc+=1
                dec=1
            elif nums[i]>nums[i+1]:
                inc=1
                dec+=1
            else:
                inc=1
                dec=1
        
            res = max(res, inc ,dec)

        return res
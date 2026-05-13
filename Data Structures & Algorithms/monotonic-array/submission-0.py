class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        n = len(nums)
        inc=dec=True
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                inc=False
            elif nums[i]<nums[i+1]:
                dec=False
        
        return inc or dec

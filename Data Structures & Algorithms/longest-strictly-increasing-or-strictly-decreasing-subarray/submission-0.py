class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        

        res = 0
        n = len(nums)
        i = j = 0
        while i<n:
            j=i
            while j<n-1 and nums[j]>nums[j+1]:
                j+=1
            res=max(res, j-i+1)
            i=j+1

        i = j = 0
        while i<n:
            j=i
            while j<n-1 and nums[j]<nums[j+1]:
                j+=1
            res=max(res, j-i+1)
            i=j+1
        
        return res
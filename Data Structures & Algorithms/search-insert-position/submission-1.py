class Solution:
    def searchInsert(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        res=n

        while l<=r:
            m = l+ (r-l)//2
            
            if nums[m]>=k:
                res = m
                r=m-1
            else:
                l=m+1
        
        return res

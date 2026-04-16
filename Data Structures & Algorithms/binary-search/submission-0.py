class Solution:
    def search(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, r = 0, n-1

        while l<=r:
            m = l + (r-l)//2
            if nums[m]==k:
                return m
            elif nums[m]>k:
                r=m-1
            else:
                l=m+1
        
        return -1

        
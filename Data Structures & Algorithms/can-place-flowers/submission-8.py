from functools import cache

class Solution:
    def canPlaceFlowers(self, nums: List[int], k: int) -> bool:
        
        n = len(nums)

        for i in range(n):
            if k<=0:
                return True
            
            l = (i==0 or nums[i-1]==0)
            r = (i==n-1 or nums[i+1]==0)

            if nums[i]==0 and l and r:
                nums[i]=1
                k-=1
        
        return k<=0

        
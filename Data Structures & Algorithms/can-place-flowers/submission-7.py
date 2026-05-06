from functools import cache

class Solution:
    def canPlaceFlowers(self, nums: List[int], k: int) -> bool:
        
        n = len(nums)

        for i in range(n):
            if nums[i]==1:
                continue
            flag=True
            for nei in [i-1, i+1]:
                if 0<=nei<n and nums[nei]==1:
                    flag=False
                    break
            
            if flag:
                nums[i]=1
                k-=1
            # print(i,flag, k)

        
        return k<1

        
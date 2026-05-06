class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        pfx = [0 for _ in range(n)]
        curr = 0
        for i in range(n):
            pfx[i]=curr
            curr+=nums[i]
        
        sfx = [0 for _ in range(n)]
        curr = 0
        for i in range(n-1, -1, -1):
            sfx[i]=curr
            curr+=nums[i]
        
        for i in range(n):
            if pfx[i]==sfx[i]:
                return i
        return -1


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        pfx = [0 for _ in range(n)]
        curr = 0
        for i in range(n):
            pfx[i]=curr
            curr+=nums[i]
        
        tot = curr

        for i in range(n):
            if pfx[i]==tot-pfx[i]-nums[i]:
                return i
            
        return -1


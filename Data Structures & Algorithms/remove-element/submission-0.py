class Solution:
    def removeElement(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        idx = 0
        for i in range(n):
            if nums[i]!=k:
                nums[i], nums[idx] = nums[idx], nums[i]
                idx+=1
        return idx

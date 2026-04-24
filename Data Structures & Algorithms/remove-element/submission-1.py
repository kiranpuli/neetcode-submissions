class Solution:
    def removeElement(self, nums: List[int], k: int) -> int:
        i = 0
        n = len(nums)
        for j in range(n):
            if nums[j]!=k:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
        
        return i
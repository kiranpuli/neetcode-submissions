class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        n = len(nums)
        seen = set()
        idx = 0
        for i,v in enumerate(nums):
            if v not in seen:
                seen.add(v)
                nums[i], nums[idx] = nums[idx], nums[i]
                idx+=1
    
        return idx
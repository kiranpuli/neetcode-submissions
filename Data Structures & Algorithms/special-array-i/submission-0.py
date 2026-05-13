class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)        
        for i in range(n-1):
            if (nums[i]&1, nums[i+1]&1) not in [(1, 0), (0, 1)]:
                return False
        return True
class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        idx = n
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                idx = i
                break

        
        nums = nums[idx+1:]+nums[:idx+1]
        print(nums)
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                return False
        return True




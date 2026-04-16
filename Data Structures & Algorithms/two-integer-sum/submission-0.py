class Solution:
    def twoSum(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[j]==k-nums[i]:
                    return [i, j]
        return [-1, -1]
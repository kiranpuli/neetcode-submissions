class Solution:
    def replaceElements(self, nums: List[int]) -> List[int]:
        M = -1
        n = len(nums)
        for i in range(n-1, -1, -1):
            tmp = M
            M = max(M, nums[i])
            nums[i]=tmp
        return nums
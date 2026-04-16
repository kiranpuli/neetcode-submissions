class Solution:
    def replaceElements(self, nums: List[int]) -> List[int]:
        M = -1
        n = len(nums)
        for i in range(n-1, -1, -1):
            tmp = nums[i]
            nums[i]=M
            M = max(tmp, M)

        nums[-1]=-1
        return nums
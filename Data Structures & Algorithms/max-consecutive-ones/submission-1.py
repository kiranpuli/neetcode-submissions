class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        res = 0
        for i in range(n):
            if nums[i]==1:
                j=i
                while j<n and nums[j]==1:
                    j+=1
                res=max(res, j-i)

        return res
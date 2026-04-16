class Solution:
    def twoSum(self, nums: List[int], k: int) -> List[int]:
        vis = {}

        for i,b in enumerate(nums):
            a = k-b
            if a in vis:
                return [vis[a], i]
            vis[b]=i
        return [-1, -1]

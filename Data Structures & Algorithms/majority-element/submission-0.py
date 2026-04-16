class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        line = n//2
        d = Counter(nums)
        for k, v in d.items():
            if v>line:
                return k
        return -1
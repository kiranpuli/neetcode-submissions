class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        d = Counter(nums)

        for k,f in d.items():
            if f>=n//2:
                return k
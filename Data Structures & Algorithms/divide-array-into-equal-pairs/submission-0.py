class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d = Counter(nums)

        for k, f in d.items():
            if f&1:
                return False
        
        return True
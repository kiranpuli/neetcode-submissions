class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        actual = sum(nums)
        expected = (1/2) * n * (n+1)
        d = expected-actual
        
        vis = set()
        dup=0
        for i in nums:
            print(i)
            if i in vis:
                dup = i
                break
            vis.add(i)

        return [dup, int(dup+d)]
class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.pfx = [0 for _ in range(n)]
        curr=0
        for i in range(n):
            curr+=nums[i]
            self.pfx[i]=curr
        print(nums)

    def sumRange(self, l: int, r: int) -> int:
        return self.pfx[r] if l<1 else self.pfx[r]-self.pfx[l-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
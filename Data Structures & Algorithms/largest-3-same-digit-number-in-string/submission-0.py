class Solution:
    def largestGoodInteger(self, nums: str) -> str:
        
        w = 3
        n = len(nums)
        d = dict()
        l=0
        res = "-1"
        for r in range(n):
            # print(l, r, d)
            if r-l+1>w:
                d[nums[l]]-=1
                if d[nums[l]]==0:
                    del d[nums[l]]
                l+=1
            
            if nums[r] not in d:
                d[nums[r]]=0

            d[nums[r]]+=1

            if r-l+1==3 and len(d.keys())==1:
                if int(nums[l:r+1])>int(res):
                    res = nums[l:r+1]

        return res if res!="-1" else ""





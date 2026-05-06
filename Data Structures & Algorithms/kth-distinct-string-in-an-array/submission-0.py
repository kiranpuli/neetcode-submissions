class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = Counter(arr)

        for c in arr:

            if d[c]==1:
                k-=1
            
            if k==0:
                return c
        return ""
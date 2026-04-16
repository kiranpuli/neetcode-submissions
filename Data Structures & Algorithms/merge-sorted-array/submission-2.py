class Solution:
    def merge(self, a: List[int], m: int, b: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = j = 0
        res= []
        while i<m and j<n:
            if a[i]<=b[j]:
                res.append(a[i])
                i+=1
            else:
                res.append(b[j])
                j+=1

        while i<m:
            res.append(a[i])
            i+=1
        
        while j<n:
            res.append(b[j])
            j+=1

        for i in range(n+m):
            a[i]=res[i]


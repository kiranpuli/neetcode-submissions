class Solution:
    def isSubsequence(self, a: str, b: str) -> bool:
        la, lb = len(a), len(b)
        mem = {}

        def solve(i, j):
            if j>=lb:
                return i==la
            
            if i==la:
                return True

            if (i,j) in mem:
                return mem[(i, j)]
            
            if a[i]==b[j]:
                mem[(i, j)] =  solve(i+1, j+1)
                return mem[(i, j)]
            else:
                mem[(i, j)] =  solve(i, j+1)
                return mem[(i, j)]
            
            
        
        return solve(0,0)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def solve(curr, i, rem):
            if curr==curr[::-1]:
                return True
            
            if i>=len(curr):
                return False

            if rem>0:
                return solve(curr, i+1, rem) or solve(curr[:i]+curr[i+1:], i+1, rem-1)
            else:
                return solve(curr, i+1, rem)

        
        return solve(list(s), 0, 1)
    

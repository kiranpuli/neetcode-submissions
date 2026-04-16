class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        stack = []

        for c in s:
            if c in d.values():
                stack.append(c)
            else:
                if not stack or stack[-1]!=d[c]:
                    return False
                stack.pop()
        
        return len(stack)==0
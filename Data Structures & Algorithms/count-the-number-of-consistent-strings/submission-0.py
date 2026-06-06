class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        res = 0
        allowed = set(allowed)
        for word in words:
            word = set(word)
            if len(word-allowed)==0:
                res+=1
        
        return res
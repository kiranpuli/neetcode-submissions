class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        allstrs = " ".join(words)
        res = []

        for word in words:
            if allstrs.count(word)>1:
                res.append(word)
        
        return res
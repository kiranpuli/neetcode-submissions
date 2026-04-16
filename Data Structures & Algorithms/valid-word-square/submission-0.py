class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        R = len(words)
        C = 0
        def getCol(i):
            nonlocal C

            res = []
            for word in words:
                C = max(C, len(word))
                if i<len(word):
                    res.append(word[i])

            return "".join(res)
        

        for k in range(max(R, C)):
            # print(words[k], getCol(k))
            if words[k]!=getCol(k):
                return False
        return True
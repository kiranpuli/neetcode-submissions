class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        d = Counter("".join(words))
        n = len(words)

        for k,v in d.items():
            if v%n!=0:
                return False
        return True
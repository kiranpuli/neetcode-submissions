class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        d = Counter("".join(words))
        n = len(words)

        return all(f%n==0 for f in d.values())
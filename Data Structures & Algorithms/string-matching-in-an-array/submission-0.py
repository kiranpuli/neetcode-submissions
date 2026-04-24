class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        res = set()
        for i in range(n):
            for j in range(i+1, n):
                if words[i] in words[j]:
                    res.add(words[i])
                elif words[j] in words[i]:
                    res.add(words[j])
        return list(res)
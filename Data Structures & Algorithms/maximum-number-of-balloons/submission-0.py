class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = Counter(text)
        t = Counter("balloon")

        mi = float('inf')

        for k,f in t.items():
            if k not in d.keys():
                return 0
            else:
                mi=min(mi,d[k]//f)
        return mi

        

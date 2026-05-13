class Solution:
    def heightChecker(self, actual: List[int]) -> int:
        expected = list(sorted(actual))
        res = 0
        for a,e in zip(actual, expected):
            if a!=e:
                res+=1
        return res
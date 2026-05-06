class Solution:
    def findDisappearedNumbers(self, b: List[int]) -> List[int]:
        n = len(b)
        a = set(range(1, n+1))

        return list(a-set(b))
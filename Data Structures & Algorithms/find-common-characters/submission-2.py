from functools import reduce

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        counters = [Counter(word) for word in words]

        res = reduce(lambda a, b: a&b, counters)
        
        return list(res.elements())

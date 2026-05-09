from collections import defaultdict

class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for word in words:
            k = "".join(list(sorted(word)))
            d[k].append(word)
        
        return list(d.values())

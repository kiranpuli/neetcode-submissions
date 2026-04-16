class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def getHash(s):
            return "".join(list(sorted(s)))

        res = defaultdict(list)
        for s in strs:
            key = getHash(s)
            res[key].append(s)
        return list(res.values())

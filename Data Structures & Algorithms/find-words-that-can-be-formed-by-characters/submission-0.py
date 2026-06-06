class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d = Counter(chars)
        res = []

        for word in words:
            req = Counter(word)
            flag=True
            for k,f in req.items():
                if k not in d:
                    flag=False
                    break
                else:
                    if d[k]<req[k]:
                        flag=False
                        break

            if flag:
                res.append(word)
        
        return sum([len(s) for s in res])

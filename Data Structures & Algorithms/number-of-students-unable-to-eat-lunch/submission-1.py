class Solution:
    def countStudents(self, pref: List[int], avail: List[int]) -> int:
        
        d = Counter(pref)

        for i in avail:
            if d[i]>0:
                d[i]-=1
            else:
                break
        
        return sum(d.values())
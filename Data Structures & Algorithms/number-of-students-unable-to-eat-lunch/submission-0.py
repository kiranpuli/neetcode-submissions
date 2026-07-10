class Solution:
    def countStudents(self, pref: List[int], avail: List[int]) -> int:
        
        while avail and pref:
            top = avail[0]
            pivot = -1
            for i,v in enumerate(pref):
                if v==top:
                    pivot=i
            if pivot==-1:
                return len(pref)
            
            pref = pref[pivot:]+pref[:pivot]
            pref.pop(0)
            avail.pop(0)
        print(pref, avail)
        return len(pref)
class Solution:
    def wordPattern(self, a: str, s: str) -> bool:
        l = dict()
        r = dict()
        b = s.split()
        i = j = 0
        while i<len(a) and j<len(b):
            x , y = a[i], b[j]
            print(x, y)
            if x not in l:
                l[x]=y
            else:
                if l[x]!=y:
                    return False
            
            if y not in r:
                r[y]=x
            else:
                if r[y]!=x:
                    return False
            i+=1
            j+=1

        if i<len(a) or j<len(b):
            return False


        return True
            

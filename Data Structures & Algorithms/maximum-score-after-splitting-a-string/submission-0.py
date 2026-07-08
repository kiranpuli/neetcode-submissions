class Solution:
    def maxScore(self, s: str) -> int:

        n = len(s)
        pre = [0 for _ in range(n)]
        curr = 0
        for i in range(n):
            if s[i]=='0':
                curr+=1
            pre[i]=curr


        sfx = [0 for _ in range(n)]
        curr=0
        for i in range(n-1, -1, -1):
            if s[i]=='1':
                curr+=1
            sfx[i]=curr
        
        res = 0
        print(pre, sfx)
        for i in range(n-1):
            res=max(res, pre[i]+sfx[i+1])
        return res


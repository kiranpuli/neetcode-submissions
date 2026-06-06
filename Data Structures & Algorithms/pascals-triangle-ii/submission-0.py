class Solution:
    def getRow(self, i: int) -> List[int]:
        if i==0:
            return [1]
        
        curr = [1]
        pre = self.getRow(i-1)

        for j in range(1, i):
            curr.append(pre[j-1]+pre[j])
        
        curr.append(1)

        return curr

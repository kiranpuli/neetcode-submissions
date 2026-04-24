class Solution:
    def generate(self, R: int) -> List[List[int]]:
        res = [[1]]

        for i in range(R-1):
            tmp = [0] + res[-1] + [0]
            newRow = []

            for j in range(len(tmp)-1):
                newRow.append(tmp[j] + tmp[j+1])

            res.append(newRow)
        
        return res
class Solution:
    def countSeniors(self, details: List[str]) -> int:

        res = 0

        for record in details:
            # phone = record[:10]
            # sex = record[10]
            age = record[11:13]
            # seat = record[13:]
            if int(age)>60:
                res+=1
        
        return res
class Solution:
    def isAnagram(self, a: str, b: str) -> bool:
        counter = [0]*26

        for i in a:
            counter[ord(i)-ord("a")]+=1
        
        for i in b:
            counter[ord(i)-ord("a")]-=1

        for i in counter:
            if i!=0:
                return False
        return True
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        m = len(nums1)
        n = len(nums2)
        res = []

        for i in range(m):
            j = nums2.index(nums1[i])
            
            tmp = -1
            for k in range(j+1, n):
                if nums2[k]>nums2[j]:
                    tmp=nums2[k]
                    break
            # print(nums1[i], j, tmp)
            res.append(tmp)
        
        return res


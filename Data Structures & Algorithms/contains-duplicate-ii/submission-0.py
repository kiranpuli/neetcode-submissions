class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        d = defaultdict(list)
        for i,v in enumerate(nums):
            d[v].append(i)

        
        for _,arr in d.items():
            for i in range(len(arr)-1):
                if arr[i+1]-arr[i]<=k:
                    return True
        
        return False
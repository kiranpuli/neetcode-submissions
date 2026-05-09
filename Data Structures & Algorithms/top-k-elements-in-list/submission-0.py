from heapq import heappush as push, heappop as pop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        d = Counter(nums)

        for n, f in d.items():
            push(heap, (f, n))
            if len(heap)>k:
                pop(heap)
        
        return [n for _, n in heap]
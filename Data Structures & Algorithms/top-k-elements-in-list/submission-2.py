import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in nums:
            freq[i] = freq.get(i,0) + 1
        
        heap = []
        
        for i,v in freq.items():
            heapq.heappush(heap,(v,i))
            
            if len(heap) > k:
                heapq.heappop(heap)
       
        res = [i[1] for i in heap]
        return res
        
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maps = dict()

        for i in nums:
            maps[i] = maps.get(i,0) + 1
        
        heap = []
        for i,v in maps.items():
            heapq.heappush(heap,(v,i))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [i[1] for i in heap]

        
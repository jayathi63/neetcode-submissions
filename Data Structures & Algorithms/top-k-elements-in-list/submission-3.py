import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_nums = dict()

        for i in nums:
            map_nums[i] = map_nums.get(i,0) + 1
        
        heap = []
        
        for i,v in map_nums.items():
            heapq.heappush(heap,[v,i])
            
            if len(heap) > k:
                heapq.heappop(heap)
            
        res = [i[1] for i in heap]
        return res

        
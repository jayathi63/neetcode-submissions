class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        res = 0
        map_nums = dict()

        for i in nums:
            map_nums[i] = 1
        
        for i in nums:

            if i-1 in map_nums and map_nums[i-1] > 1:
                # map_nums[i] = map_nums[i-1] -1
                continue
            
            j = i+1
            c = 1
            while(j in map_nums):
                c += map_nums[j]
                j += map_nums[j]
            
            res = max(res,c)
            map_nums[i] = c
        
        return res


        


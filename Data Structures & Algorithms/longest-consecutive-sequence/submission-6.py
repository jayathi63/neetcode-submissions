class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        map_nums = dict()
        for i in nums:
            map_nums[i] = 1
        n = len(nums)
        res = 0
        key = -1
        
        for i in range(n):
            
            c = 1
            j = nums[i]+1

            if nums[i]-1 in map_nums and map_nums[nums[i]-1] >= 1:
                continue
            
            while(j in map_nums):
                c += map_nums[j]
                j+=map_nums[j]
   
            map_nums[nums[i]] = c
            res = max(res,c)
            
        
        return res


        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        map_nums = dict()
        # for i in nums:
        #     map_nums[i] = 1
        n = len(nums)
        res = 0
        set_nums = set(nums)
        # key = -1
        
        for i in range(n):
            
            c = 1
            j = nums[i]+1

            if nums[i]-1 in map_nums:
                map_nums[nums[i]] = map_nums[nums[i]-1]-1
                continue
            # print(map_nums)
            while(j in set_nums):
                if j in map_nums:
                    c += map_nums[j]
                    j += map_nums[j]
                    continue
                c += 1
                j+= 1
   
            map_nums[nums[i]] = c
            res = max(res,c)
            
        
        return res


        
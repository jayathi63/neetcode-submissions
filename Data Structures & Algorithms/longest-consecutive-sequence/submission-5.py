class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        map_nums = dict()
        for i in nums:
            map_nums[i] = 1
        n = len(nums)
        res = 0
        key = -1
        # print(set_nums)
        for i in range(n):
            # print(i)
            c = 1
            j = nums[i]+1
            # print(key,j,res)
            # print(nums[key],j,nums[key]+(res))
            # if key!=-1 and nums[key] <= j <= nums[key]+(res):
            #     continue
            
            # print(j)
            while(j in map_nums):
                c += map_nums[j]
                j+=map_nums[j]

            # print(map_nums)
            # print(j,c)
            map_nums[nums[i]] = c
            res = max(res,c)
            if res == c:
                key = i



        
        return res


        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        res = 0
        

        for i in nums:

            if i-1 not in nums:
                c = 1
                j = i+1
                while j in nums:
                    c += 1
                    j += 1
            
                if res < c:
                    res = c
        
        return res
            


        


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        max_len = 0

        for i in nums:
            lens = 1
            if i-1 not in nums_set:
                
                j = i+1
                while j in nums_set:
                    j += 1
                    lens += 1
                
            max_len = max(max_len,lens)
        
        return max_len
                



        


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        max_len = 0

        for i in nums:
            
            if i-1 not in nums_set:
                lens = 0
                
                while i+lens in nums_set:
                    lens += 1
                
                max_len = max(max_len,lens)
        
        return max_len
                



        


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res = set()

        for i in range(n):
            rem = 0 - nums[i]
            seen = dict()

            target = rem

            for j in range(i+1,n):
                
                k = target - nums[j]

                if k in seen:
                    res.add(tuple(sorted([nums[i],nums[j],nums[seen[k]]])))
                    
            
                seen[nums[j]] = j
        
        res = [list(i) for i in res]
        return res


        
        

        
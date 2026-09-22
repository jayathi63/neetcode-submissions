class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = dict()
        n = len(nums)

        for i in range(n):
            rem = target - nums[i]

            if rem in seen:
                return [seen[rem],i]
            
            seen[nums[i]] = i
        
        return []
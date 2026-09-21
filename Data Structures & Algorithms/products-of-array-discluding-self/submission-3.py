class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zero_count = 0
        prod = 1
        res = []
        for i in nums:
            if i == 0:
                zero_count+=1
            else:
                prod *= i
        
        if zero_count >= 2:
            res = [0] * n
            return res
        
        for i in range(n):
            if zero_count == 0:
                res.append(prod//nums[i])
            else:
                if nums[i] == 0:
                    res.append(prod)
                else:
                    res.append(0)
        return res
                




        
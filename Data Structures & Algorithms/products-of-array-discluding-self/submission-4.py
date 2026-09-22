class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        prod = 1
        n = len(nums)
        res = []

        for i in nums:
            if i == 0:
                zero_count += 1
            else:
                prod *= i
        
        if zero_count >= 2:
            return [0] * n
        
        for i in nums:
            if zero_count == 0:
                res.append(int(prod//i))
            else:
                if i == 0:
                    res.append(prod)
                else:
                    res.append(0)
        return res






        
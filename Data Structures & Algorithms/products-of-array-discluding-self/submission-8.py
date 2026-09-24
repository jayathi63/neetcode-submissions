class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_c = 0
        prod = 1

        for i in nums:
            if i == 0:
                zero_c += 1
            else:
                prod *= i
            
        
        n = len(nums)

        if zero_c >= 2:
            return [0]*n
        
        res = []
        for i in nums:
            if zero_c == 1:
                if i == 0:
                    res.append(prod)
                else:
                    res.append(0)
            else:
                res.append(prod//i)
        
        return res



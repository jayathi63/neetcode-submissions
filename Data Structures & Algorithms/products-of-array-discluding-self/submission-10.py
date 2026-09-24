class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre = []
        prod = 1

        for i in nums:
            pre.append(prod)
            prod *= i
        
        prod = 1
        n = len(nums)

        for i in range(n-1,-1,-1):
            pre[i] = prod * pre[i]
            prod *= nums[i]
        
        return pre


        




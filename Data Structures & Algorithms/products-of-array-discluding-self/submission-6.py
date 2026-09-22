class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        n = len(nums)
        post = [0] * n
        prod = 1
        for i in nums:
            pre.append(prod)
            prod *= i
        
        prod = 1
        for i in range(n-1,-1,-1):
            post[i] = prod * pre[i]
            prod *= nums[i] 
        
        # res = [0] * n
        # for i in range(n):
        #     res[i] = pre[i] * post[i]
        
        return post



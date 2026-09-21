class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        pre = []
        post = [0] * n
        prod = 1
        for i in nums:
            pre.append(prod)
            prod *= i
        
        prod = 1
        for j in range(n-1,-1,-1):
            post[j] = prod
            prod *= nums[j]
        
        # print(pre)
        # print(post)

        for i in range(0,n):
            res.append(pre[i] * post[i])
        
        return res



        
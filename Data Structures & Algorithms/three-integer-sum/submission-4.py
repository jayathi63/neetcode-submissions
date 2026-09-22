class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res = []
        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            rem = 0 - nums[i]
            

            target = rem

            
            
            l = i+1
            r = n-1

            while(l < r):
                cur_sum = nums[l] + nums[r]

                if cur_sum == target:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif cur_sum > target:
                    r-=1
                else:
                    l+=1
        
        
        return res


        
        

        
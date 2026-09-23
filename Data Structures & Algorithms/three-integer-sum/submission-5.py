class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums = sorted(nums)
        res = []
        n = len(nums)
        i = 0

        print(nums)

        while(i<n):

            l = i+1
            r = n-1

            target = 0 - nums[i]

            while(l < r):

                sums = nums[l] + nums[r]

                if sums > target:
                    r-=1
                elif sums < target:
                    l+=1
                    
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    
                    l+=1
                    r-=1
                    while(l<n and nums[l] == nums[l-1]):
                        l += 1
                    while(r>0 and nums[r] == nums[r+1]):
                        r -= 1
            i+=1
            while(i<n and nums[i] == nums[i-1]):
                        i += 1
        return res
            

                
                

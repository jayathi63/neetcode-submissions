class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        n = len(nums)
        nums = sorted(nums)
        res = []
        i = 0

        while i < n:
                
            l = i+1
            h = n-1

            target = 0 - nums[i]

            while(l < h):

                sums = nums[l] + nums[h]

                if target == sums:
                    res.append([nums[i],nums[l],nums[h]])
                    l += 1
                    h -= 1

                    while(l< n and nums[l] == nums[l-1]):
                        l += 1
                    while(h >= 0 and nums[h] == nums[h+1]):
                        h -= 1
                    
                elif target < sums:
                    h -= 1
                else:
                    l += 1

            i += 1

            while(i < n and nums[i] == nums[i-1]):
                i += 1
        
        return res

                





class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res = []
        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            rem = 0 - nums[i]
            # seen = dict()

            target = rem

            # for j in range(i+1,n):
                
            #     k = target - nums[j]

            #     if k in seen:
            #         res.add(tuple(sorted([nums[i],nums[j],nums[seen[k]]])))
                    
            
                # seen[nums[j]] = j
            
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


        
        

        
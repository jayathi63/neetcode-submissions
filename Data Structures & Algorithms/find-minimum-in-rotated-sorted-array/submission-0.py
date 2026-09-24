class Solution:
    def findMin(self, nums: List[int]) -> int:

        minm = nums[0]

        for i in nums:
            if i < minm:
                minm = i
        return minm
        
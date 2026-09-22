class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxm = -1
        l = 0
        r = n-1
        while(l < r):
            h = min(heights[l],heights[r])
            w = r - l
            maxm = max(maxm, h*w)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxm

        
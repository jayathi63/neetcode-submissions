class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        i = 0
        j = n - 1
        maxm = -1



        while(i < j):

            w = j-i
            h = min(heights[i],heights[j])

            area = w * h

            if area > maxm:
                maxm = area
            
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        
        return maxm

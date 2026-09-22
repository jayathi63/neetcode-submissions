class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        res = 0
        for i in range(n):
            max_prof = 0
            j = i+1
            while(j < n and prices[j] > prices[i]):
                prof = prices[j] - prices[i]
                max_prof = max(max_prof,prof)
                j += 1
            res = max(max_prof,res)
        
        return res
                

        
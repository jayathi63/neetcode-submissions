class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_prof = 0
        min_buy = prices[0]
        for i in range(1,n):
            prof = prices[i] - min_buy
            max_prof = max(max_prof, prof)

            min_buy = min(min_buy, prices[i])
        

            
        
        return max_prof
                

        
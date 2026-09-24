class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        i = 0

        j = 0
        min_buy = prices[0]
        max_p = 0

        while(j < n):

            if min_buy > prices[j]:
                min_buy = prices[j]

            b = min_buy
            s = prices[j]

            prof = s-b

            if prof > max_p:
                max_p = prof
            
            j+=1

        return max_p

                

        
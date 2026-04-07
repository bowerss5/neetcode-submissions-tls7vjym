class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = sell - buy  
        profit, buy = 0, 100
        
        for sell in prices:
            if sell < buy:
                buy = sell
            if sell - buy > profit:
                profit = sell - buy
            
        return max(0, profit)


        
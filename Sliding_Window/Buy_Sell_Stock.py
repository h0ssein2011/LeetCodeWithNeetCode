#Best Time to Buy and Sell Stock
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

#Brute Force Solution with O(n) time complexity
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = min(prices)
        idx_min_price = prices.index(minPrice)
        prices = prices[idx_min_price:]
        max_price = max(prices)
        
        return max(max_price - minPrice,0)

# Sliding window Solution with O(n) time complexity
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r = 0 ,  1
        
        Max_profit = 0
        
        while r < len(prices) :
            # print( 'L:',l,'R:',r )
            #check profitable transaction
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                Max_profit = max(Max_profit , profit)
            else :
                l = r
            r += 1
            # print('Max_profit-->',Max_profit)

        return Max_profit
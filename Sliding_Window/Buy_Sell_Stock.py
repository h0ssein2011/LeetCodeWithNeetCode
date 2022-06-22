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

# Two Pointers Solution with O(n) time complexity
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r = 0 , len(prices) - 1
        min_price , max_price = 0 , 0
        profit = max_price - min_price
        while l < r :
            print(l,'-->',r)
            if prices[l+1] <  prices[l]:
                
                min_price = prices[l+1]
                
            if prices[r - 1] >  prices[r]:
                
                max_price = prices[r-1]
                 
            l , r = l+1 , r - 1
            print('max_is:',max_price)
            print('min_is:',min_price)
            
        return max_price - min_price
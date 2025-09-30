"""
121. Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given 
stock on the ith day.

You want to maximize your profit by choosing a single day to buy one 
stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you 
cannot achieve any profit, return 0.

 

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), 
profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because 
you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit 
= 0.
 

Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104
"""

# Key Note:
# 1. We can only buy and sell stock for one time, so we need to try to 
# find the min and max prices.
# 2. The point is we can just simply iterate through it and find out 
# the max and min ones, because the max ones may be before min ones. 
# we cant use two for loops to find the max for each min too because
# big O is too big.
# Instead we can just track current max_profit, the max_profit can be
# calculated by cureent_price - min_price. we just need to maintain
# min_prices and update max_prices.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prices = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_prices:
                min_prices = prices[i]
            max_profit = max(max_profit, prices[i] - min_prices)
        return max_profit

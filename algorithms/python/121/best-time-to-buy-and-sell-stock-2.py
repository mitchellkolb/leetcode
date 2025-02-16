

# 121
# best-time-to-buy-and-sell-stock

"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

 

Constraints:

    1 <= prices.length <= 105
    0 <= prices[i] <= 104


"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 1:
            return 0
        
        left, right, max = 0, 1, 0

        while right < len(prices):
            if prices[left] < prices[right]:
                current = prices[right] - prices[left]
                if current > max:
                    max = current
                right += 1
            else:
                left = right
                right += 1
            
        return max
           



solution = Solution()
tests = [[2,1,2,1,0,1,2], [1], [2,3], [4,2], [2,4,1], [7,6,4,3,1], [7,1,5,3,6,4]]
for test in tests:
    print(solution.maxProfit(test))
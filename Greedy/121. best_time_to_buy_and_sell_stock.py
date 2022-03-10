"""
我们需要找出给定个数组中两个数字之间的最大差值（最大利润）， 此外第二个数字（卖出） 必须大于第一个数字（买入）
"""
# 暴力
def maxProfix(prices):
    ans = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            ans = max(ans, prices[j] - prices[i])
    return ans


# 一次遍历
def maxProfit(prices):
    min_price = float("inf")
    max_profit = 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
    return max_profit
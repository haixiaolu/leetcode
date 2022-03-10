"""
1. One Pass
    - 遍历整个股票交易日价格列表 price， 策略时所有上涨交易日都买卖， 所有下降交易日都不买卖
    - 设tmp为第i - 1日买入与第i日卖出赚取的利润。 即tmp = prices[i] - prices[i - 1]
    - 当该天利润为正tmp > 0, 则将利润加入总利润profit， 当利润为0或为负， 则直接跳过
    - 遍历完成后， 返回总利润profit
"""


def maxProfit(prices):
    profit = 0
    for i in range(i, len(prices)):
        tmp = prices[i] - prices[i - 1]
        if tmp > 0:
            profit += tmp
    return profit

"""
Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.
"""
def buy_and_sell_high_profile(stock):
    current_max, max_profit = 0, 0
    for price in reversed(stock):
        current_max = max(price, current_max)
        current_profit = current_max - price
        max_profit = max(max_profit, current_profit)
    
    return max_profit


print(buy_and_sell_high_profile([9, 11, 8, 5, 7, 10]))
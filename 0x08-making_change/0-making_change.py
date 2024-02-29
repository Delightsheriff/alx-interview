#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """
    determine the fewest number of coins needed to meet a given amount total
    """
    if total <= 0:
        return 0
    coins = sorted(coins, reverse=True)
    count = 0
    coin_sum = 0
    for coin in coins:
        while coin + coin_sum <= total:
            coin_sum += coin
            count += 1
        if coin_sum == total:
            return count
    if coin_sum == total:
        return count
    return -1

#!/usr/bin/python3
"""0x08-making_change module"""
 
def makeChange(coins, total):
    """make change function """
    if total <= 0:
        return 0

    # Initialize a table
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin value
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

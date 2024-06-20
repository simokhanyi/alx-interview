#!/usr/bin/python3
"""
Module for making change problem.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.

    Args:
        coins (list of int): The values of the coins.
        total (int): The total amount to meet.

    Returns:
        int: The fewest number of coins needed to meet total,
             or -1 if total cannot be met by any number of coins.
    """
    if total <= 0:
        return 0

    # Initialize dp array with inf (assuming float('inf') for infinity)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1


# Test cases
if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))

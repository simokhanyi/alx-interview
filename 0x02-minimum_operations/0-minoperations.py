#!/usr/bin/python3
"""
minimum operations
"""


def minOperations(n):
    if n <= 1:
        return n

    # Initialize an array to store the minimum number of operations needed
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = float('inf')  # Initialize to infinity
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n] if dp[n] != float('inf') else 0


# Test cases
n = 4
print(
    "Min number of operations to reach {} char: {}".format(n, minOperations(n))
)

n = 12
print(
    "Min number of operations to reach {} char: {}".format(n, minOperations(n))
)

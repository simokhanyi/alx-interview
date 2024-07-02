#!/usr/bin/python3
""" Prime game module
"""


def isWinner(x, nums):
    """
    Determines the winner of a game played over x rounds with varying numbers.

    Parameters:
    x (int): The number of rounds to be played.
    nums (list of int): List containing the upper limits (n) for each round.

    Returns:
    str: The name of the player ("Maria" or "Ben") who won the most rounds.
         If the result is a tie, returns None.
    """
    if x <= 0 or not nums:
        return None

    def generate_primes(n):
        """
        Generates a list of prime numbers up to n.
        Parameters:
        n (int): The upper limit for generating prime numbers.

        Returns:
        list of int: A list of prime numbers up to n.
        """
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        primes = [p for p in range(n + 1) if is_prime[p]]
        return primes

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
            continue

        primes = generate_primes(n)
        move_count = 0

        while primes:
            move_count += 1
            prime_to_remove = primes[0]
            primes = [p for p in primes if p % prime_to_remove != 0]

        if move_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


# Testing the function
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

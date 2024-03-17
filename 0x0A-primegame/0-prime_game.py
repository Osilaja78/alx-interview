#!/usr/bin/python3
"""0-prime_game.py module"""


def isWinner(x, nums):
    """Min function for gameplay"""

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def generate_primes(n):
        """Generate prime numbers"""

        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def can_player_win(n):
        """Check if player wins"""

        primes = generate_primes(n)
        if len(primes) % 2 == 0:
            return "Maria"
        else:
            return "Ben"

    maria_wins = 0
    ben_wins = 0
    for i in range(x):
        winner = can_player_win(nums[i])
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

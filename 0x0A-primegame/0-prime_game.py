#!/usr/bin/python3
"""0-prime_game.py module"""

from typing import List


def isWinner(x: int, nums: List[int]) -> str:
    """
    This function determines the winner of the game based on the
    number of rounds (x) and the initial set of numbers (nums).

    Args:
        x: Number of rounds
        nums: List of consecutive integers

    Returns:
        str: Name of the winner ("Maria" or "Ben") or None if
        winner cannot be determined
    """

    maria_wins = 0
    ben_wins = 0

    for _ in range(x):
        if len(nums) == 1:
            ben_wins += 1
            continue

    smallest_prime = next(num for num in nums if is_prime(num))

    nums = [num for num in nums if num % smallest_prime != 0]

    has_move_for_ben = any(is_prime(num) for num in nums)

    if not has_move_for_ben:
        maria_wins += 1
    else:
        ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None


def is_prime(num: int) -> bool:
    """
    This helper function checks if a number is prime.
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

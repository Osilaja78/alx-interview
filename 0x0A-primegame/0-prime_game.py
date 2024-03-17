#!/usr/bin/python3
"""0-prime_game.py module"""


def isWinner(x, nums):
    """Main function for gameplay"""

    scores = [0, 0]
    current_player = 0
    remaining_nums = set(range(1, 10001))

    primes = set()

    for num in range(2, 10001):
        if num not in primes:
            primes.add(num)
            for multiple in range(num * 2, 10001, num):
                primes.add(multiple)

    for i in range(x):
        n = nums[i] if i < len(nums) else 10000
        remaining_nums = remaining_nums - set(range(1, n + 1))
        prime_nums = primes & remaining_nums

        if not prime_nums:
            if current_player == 0:
                scores[current_player] += 1
            else:
                scores[current_player] += 1
        else:
            smallest_prime = min(prime_nums)
            remaining_nums -= set(range(smallest_prime, n + 1, smallest_prime))
            scores[current_player] += 1
    current_player = 1 - current_player

    if scores[0] > scores[1]:
        return "Maria"
    elif scores[0] < scores[1]:
        return "Ben"
    else:
        return None

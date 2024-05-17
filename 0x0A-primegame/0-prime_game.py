#!/usr/bin/python3
"""Module that determines the winner of a game of prime"""


def isWinner(x, nums):
    """Identifies prime numbers in a given array"""
    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    primes = sieve(max_n)
    prime_set = set(primes)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
            continue

        current_set = set(range(1, n + 1))
        maria_turn = True

        while current_set:
            move_made = False
            for prime in primes:
                if prime in current_set:
                    current_set -= set(range(prime, n + 1, prime))
                    move_made = True
                    break

            if not move_made:
                if maria_turn:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            maria_turn = not maria_turn

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


def sieve(n):
    """Helper function to generate list of
    primes up to n using Sieve of Eratosthenes
    """
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    primes = []
    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
    return primes

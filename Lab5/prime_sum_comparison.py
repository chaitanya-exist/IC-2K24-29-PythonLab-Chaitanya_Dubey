"""Lab 5 / Problem 1: Compare prime-sum algorithms."""

from math import isqrt
from time import perf_counter


def prime_sum_naive(limit: int) -> int:
    """Sum primes strictly below limit using every possible divisor."""
    total = 0
    for number in range(2, limit):
        prime = True
        for divisor in range(2, number):
            if number % divisor == 0:
                prime = False
                break
        if prime:
            total += number
    return total


def prime_sum_sqrt(limit: int) -> int:
    """Sum primes below limit with divisors checked only to sqrt(number)."""
    total = 0
    for number in range(2, limit):
        if number == 2:
            total += number
            continue
        if number % 2 == 0:
            continue
        prime = True
        for divisor in range(3, isqrt(number) + 1, 2):
            if number % divisor == 0:
                prime = False
                break
        if prime:
            total += number
    return total


def prime_sum_sieve(limit: int) -> int:
    """Sum primes strictly below limit using the Sieve of Eratosthenes."""
    if limit <= 2:
        return 0
    is_prime = [True] * limit
    is_prime[0:2] = [False, False]
    for number in range(2, isqrt(limit - 1) + 1):
        if is_prime[number]:
            first_multiple = number * number
            is_prime[first_multiple:limit:number] = [False] * len(range(first_multiple, limit, number))
    return sum(index for index, prime in enumerate(is_prime) if prime)


def timed_call(function, limit: int):
    start = perf_counter()
    result = function(limit)
    return result, perf_counter() - start


def main() -> None:
    try:
        limit = int(input("Enter N (prime numbers strictly below N): "))
        if limit < 0:
            raise ValueError
    except ValueError:
        print("Please enter a non-negative whole number.")
        return

    methods = [
        ("Naive trial division", prime_sum_naive),
        ("Square-root trial division", prime_sum_sqrt),
        ("Sieve of Eratosthenes", prime_sum_sieve),
    ]
    results = []
    for label, method in methods:
        value, elapsed = timed_call(method, limit)
        results.append(value)
        print(f"{label}: sum={value}, time={elapsed:.8f} seconds")

    if len(set(results)) == 1:
        print("Check: all three methods returned the same sum.")
    else:
        print("Warning: results do not match. Review the implementations.")

    if limit > 10_000:
        print("Note: naive trial division can become very slow for large N.")


if __name__ == "__main__":
    main()

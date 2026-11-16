"""Lab 4: Sum of prime numbers up to N and measure execution time."""

from math import isqrt
from time import perf_counter


def is_prime(number: int) -> bool:
    """Return True when number is prime, using trial division up to sqrt(n)."""
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for divisor in range(3, isqrt(number) + 1, 2):
        if number % divisor == 0:
            return False
    return True


def sum_primes_up_to(limit: int) -> int:
    """Return the sum of all primes less than or equal to limit."""
    return sum(value for value in range(2, limit + 1) if is_prime(value))


def main() -> None:
    try:
        limit = int(input("Enter the upper limit (N): "))
        if limit < 0:
            print("Please enter a non-negative integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    start = perf_counter()
    total = sum_primes_up_to(limit)
    elapsed = perf_counter() - start

    print(f"Sum of prime numbers up to {limit}: {total}")
    print(f"Execution time: {elapsed:.8f} seconds")


if __name__ == "__main__":
    main()

# Lab 4 — Sum of Prime Numbers with Runtime Analysis

## Objective
Accept an integer `N`, calculate the sum of every prime number from 2 through `N` (inclusive), and report the execution time.

## Approach
- Reject values below 2 as non-prime.
- Handle 2 separately and skip even divisors.
- Test odd divisors only up to the square root of each candidate.
- Use `time.perf_counter()` to measure elapsed time.

## Run
```bash
python prime_sum.py
```

## Example
```text
Enter the upper limit (N): 10
Sum of prime numbers up to 10: 17
Execution time: ... seconds
```

The expected prime numbers are 2, 3, 5 and 7. Execution time varies by computer and should be recorded from your own run.

## Complexity
For each candidate, primality testing checks at most O(√N) divisors. The overall upper-bound time complexity is O(N√N), with O(1) auxiliary space apart from the generator/iteration state.

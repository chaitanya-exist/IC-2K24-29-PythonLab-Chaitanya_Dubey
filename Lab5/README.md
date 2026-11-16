# Lab 5 — Algorithmic Optimization and Benchmarking

## Overview
This lab compares straightforward solutions with more efficient algorithms on three problems. Runtime measurements are collected on the same machine; therefore, actual timings will vary.

## Problems
| Problem | Straightforward method | Optimized method |
|---|---|---|
| Sum of primes strictly below N | Test every divisor | Square-root trial division and Sieve of Eratosthenes |
| Count pairs with a target sum | Nested loops, O(n²) | One-pass frequency dictionary, average O(n) |
| K-th smallest pairwise sum (i < j) | Generate all sums and sort | Binary search over sum values with two-pointer counting |

## Files
- `prime_sum_comparison.py`
- `count_pairs_target_sum.py`
- `kth_pairwise_sum.py`
- Three matching Jupyter notebooks for guided execution and notes.

## Run from a terminal
```bash
python prime_sum_comparison.py
python count_pairs_target_sum.py
python kth_pairwise_sum.py
```

## Run the notebooks
Install Jupyter once, then start it from this folder:
```bash
python -m pip install notebook
jupyter notebook
```
Open each `.ipynb` file and select **Run All**.

## Notes
- Lab 5 uses the phrase “strictly below N”: N itself is excluded.
- The naive prime method is intentionally slower. Use a moderate N when comparing all three versions.
- The k-th pairwise sum uses distinct index pairs with `i < j`; equal values at different indices are still valid pairs.
- Do not copy benchmark numbers from another computer. Record your own results.

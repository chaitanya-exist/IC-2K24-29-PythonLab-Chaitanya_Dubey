"""Lab 5 / Problem 3: Find the k-th smallest pair sum for i < j."""

from time import perf_counter


def kth_sum_naive(numbers: list[int], k: int) -> int:
    """Build every pair sum, sort the values, and return the k-th one."""
    pair_sums = [
        numbers[i] + numbers[j]
        for i in range(len(numbers))
        for j in range(i + 1, len(numbers))
    ]
    if not 1 <= k <= len(pair_sums):
        raise ValueError(f"k must be between 1 and {len(pair_sums)}")
    pair_sums.sort()
    return pair_sums[k - 1]


def count_pairs_at_most(sorted_numbers: list[int], value: int) -> int:
    """Count pairs i < j whose sum is <= value in O(n) time."""
    count = 0
    right = len(sorted_numbers) - 1
    for left in range(len(sorted_numbers)):
        while left < right and sorted_numbers[left] + sorted_numbers[right] > value:
            right -= 1
        if left < right:
            count += right - left
    return count


def kth_sum_optimized(numbers: list[int], k: int) -> int:
    """Binary-search the answer range, counting eligible pairs per midpoint."""
    if len(numbers) < 2:
        raise ValueError("At least two numbers are required.")
    pair_count = len(numbers) * (len(numbers) - 1) // 2
    if not 1 <= k <= pair_count:
        raise ValueError(f"k must be between 1 and {pair_count}")

    values = sorted(numbers)
    low = values[0] + values[1]
    high = values[-2] + values[-1]

    while low < high:
        middle = (low + high) // 2
        if count_pairs_at_most(values, middle) >= k:
            high = middle
        else:
            low = middle + 1
    return low


def main() -> None:
    try:
        numbers = [int(item) for item in input("Enter at least two integers: ").split()]
        k = int(input("Enter k (1-based position): "))
    except ValueError:
        print("Please enter valid integers.")
        return

    for label, method in (("Generate and sort", kth_sum_naive), ("Binary search + two pointers", kth_sum_optimized)):
        start = perf_counter()
        try:
            result = method(numbers, k)
        except ValueError as error:
            print(error)
            return
        elapsed = perf_counter() - start
        print(f"{label}: {result}, {elapsed:.8f} seconds")


if __name__ == "__main__":
    main()

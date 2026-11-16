"""Lab 5 / Problem 2: Count index pairs whose values add to a target."""

from time import perf_counter


def count_pairs_naive(numbers: list[int], target: int) -> int:
    """Check every index pair (i, j), where i < j."""
    count = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                count += 1
    return count


def count_pairs_hashmap(numbers: list[int], target: int) -> int:
    """Count pairs in one pass using previously seen values."""
    seen: dict[int, int] = {}
    count = 0
    for value in numbers:
        complement = target - value
        count += seen.get(complement, 0)
        seen[value] = seen.get(value, 0) + 1
    return count


def main() -> None:
    try:
        numbers = [int(item) for item in input("Enter integers separated by spaces: ").split()]
        target = int(input("Enter target sum: "))
    except ValueError:
        print("Please enter valid integers.")
        return

    for label, method in (("Nested loops", count_pairs_naive), ("Hash map", count_pairs_hashmap)):
        start = perf_counter()
        count = method(numbers, target)
        elapsed = perf_counter() - start
        print(f"{label}: {count} pair(s), {elapsed:.8f} seconds")


if __name__ == "__main__":
    main()

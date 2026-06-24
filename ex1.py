import time
import random
import csv


def interpolation_search(arr, target):
    """
    Interpolation Search Algorithm
    Time Complexity: O(log log n) average, O(n) worst case
    Space Complexity: O(1)
    """

    low, high = 0, len(arr) - 1
    comparisons = 0

    while low <= high and arr[low] <= target <= arr[high]:
        comparisons += 1

        if low == high:
            if arr[low] == target:
                return low, comparisons
            return -1, comparisons

        # Interpolation Formula
        pos = low + int(
            ((target - arr[low]) * (high - low))
            / (arr[high] - arr[low])
        )

        if arr[pos] == target:
            return pos, comparisons
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1, comparisons


def binary_search(arr, target):
    """Binary Search for comparison"""

    low, high = 0, len(arr) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1

        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


def performance_analysis():
    sizes = [100, 500, 1000, 5000, 10000, 100000]

    print(
        f"{'Size':<10} {'IS Time(ms)':<14} {'BS Time(ms)':<14} "
        f"{'IS Comparisons':<16} {'BS Comparisons':<16}"
    )
    print("-" * 75)

    for size in sizes:
        arr = sorted(random.sample(range(size * 10), size))
        target = arr[random.randint(0, size - 1)]

        # Interpolation Search timing
        start = time.perf_counter()

        for _ in range(100):
            idx_is, comp_is = interpolation_search(arr, target)

        is_time = (time.perf_counter() - start) * 1000 / 100

        # Binary Search timing
        start = time.perf_counter()

        for _ in range(100):
            idx_bs, comp_bs = binary_search(arr, target)

        bs_time = (time.perf_counter() - start) * 1000 / 100

        print(
            f"{size:<10} {is_time:<14.6f} {bs_time:<14.6f} "
            f"{comp_is:<16} {comp_bs:<16}"
        )


# Main
arr = [2, 5, 10, 15, 23, 33, 43, 60, 75, 90, 105, 120]
target = 35

idx, comp = interpolation_search(arr, target)

print("Array:", arr)
print("Searching for:", target)
print()

if idx != -1:
    print(f"Found at index {idx}. Comparisons: {comp}")
else:
    print("Not found")

print()
performance_analysis()
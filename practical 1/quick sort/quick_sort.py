"""
Quick Sort Algorithm Implementation in Python.

Time Complexity:
    - Best Case: O(n log n)
    - Average Case: O(n log n)
    - Worst Case: O(n^2)

Space Complexity:
    - O(log n) Auxiliary Space for call stack (In-place partition scheme)
"""

def partition(arr: list, low: int, high: int) -> int:
    """
    Lomuto partition scheme: Takes last element as pivot, places
    the pivot element at its correct position in sorted array, and places
    all smaller elements to left of pivot and all greater elements to right.
    """
    pivot = arr[high]
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_helper(arr: list, low: int, high: int) -> None:
    """
    Recursive helper function to execute Quick Sort within bounds [low, high].
    """
    if low < high:
        # pi is partitioning index, arr[p] is now at right place
        pi = partition(arr, low, high)

        # Separately sort elements before partition and after partition
        quick_sort_helper(arr, low, pi - 1)
        quick_sort_helper(arr, pi + 1, high)


def quick_sort(arr: list) -> list:
    """
    Sorts an array in non-decreasing order using the Quick Sort algorithm.

    Parameters:
        arr (list): List of elements to be sorted.

    Returns:
        list: The sorted list.
    """
    quick_sort_helper(arr, 0, len(arr) - 1)
    return arr


if __name__ == "__main__":
    sample_data = [10, 7, 8, 9, 1, 5]
    print("Original Array:", sample_data)
    sorted_data = quick_sort(sample_data.copy())
    print("Sorted Array (Quick Sort):", sorted_data)

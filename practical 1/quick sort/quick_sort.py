"""
Quick Sort Algorithm Implementation in Python.

Time Complexity:
    - Best Case: O(n log n)
    - Average Case: O(n log n)
    - Worst Case: O(n^2)

Space Complexity:
    - O(log n)
"""

def partition(arr: list, low: int, high: int) -> int:

    pivot = arr[high]
    i = low - 1 

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
        pi = partition(arr, low, high)

        quick_sort_helper(arr, low, pi - 1)
        quick_sort_helper(arr, pi + 1, high)


def quick_sort(arr: list) -> list:

    quick_sort_helper(arr, 0, len(arr) - 1)
    return arr


if __name__ == "__main__":
    sample_data = [10, 7, 8, 9, 1, 5]
    print("Original Array:", sample_data)
    sorted_data = quick_sort(sample_data.copy())
    print("Sorted Array (Quick Sort):", sorted_data)

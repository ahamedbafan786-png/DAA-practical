"""
Bubble Sort Algorithm Implementation in Python.

Time Complexity:
    - Best Case: O(n) when array is already sorted
    - Average Case: O(n^2)
    - Worst Case: O(n^2)

Space Complexity:
    - O(1) Auxiliary Space (In-place sorting algorithm)
"""

def bubble_sort(arr: list) -> list:
    """
    Sorts an array in non-decreasing order using the Bubble Sort algorithm.

    Parameters:
        arr (list): List of elements to be sorted.

    Returns:
        list: The sorted list.
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no elements were swapped in inner loop, array is sorted
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    sample_data = [64, 34, 25, 12, 22, 11, 90]
    print("Original Array:", sample_data)
    sorted_data = bubble_sort(sample_data.copy())
    print("Sorted Array (Bubble Sort):", sorted_data)

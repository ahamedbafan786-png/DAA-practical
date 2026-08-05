"""
Selection Sort Algorithm Implementation in Python.

Time Complexity:
    - Best Case: O(n^2)
    - Average Case: O(n^2)
    - Worst Case: O(n^2)

Space Complexity:
    - O(1) Auxiliary Space (In-place sorting algorithm)
"""

def selection_sort(arr: list) -> list:
    """
    Sorts an array in non-decreasing order using the Selection Sort algorithm.

    Parameters:
        arr (list): List of elements to be sorted.

    Returns:
        list: The sorted list.
    """
    n = len(arr)
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


if __name__ == "__main__":
    sample_data = [64, 25, 12, 22, 11]
    print("Original Array:", sample_data)
    sorted_data = selection_sort(sample_data.copy())
    print("Sorted Array (Selection Sort):", sorted_data)

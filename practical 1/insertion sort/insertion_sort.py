"""
Insertion Sort Algorithm Implementation in Python.

Time Complexity:
    - Best Case: O(n) when array is already sorted
    - Average Case: O(n^2)
    - Worst Case: O(n^2)

Space Complexity:
    - O(1) Auxiliary Space (In-place sorting algorithm)
"""

def insertion_sort(arr: list) -> list:
    """
    Sorts an array in non-decreasing order using the Insertion Sort algorithm.

    Parameters:
        arr (list): List of elements to be sorted.

    Returns:
        list: The sorted list.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    sample_data = [12, 11, 13, 5, 6]
    print("Original Array:", sample_data)
    sorted_data = insertion_sort(sample_data.copy())
    print("Sorted Array (Insertion Sort):", sorted_data)

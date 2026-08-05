"""
Insertion Sort Algorithm Implementation in Python.

Time Complexity:
    - Best Case: O(n) when array is already sorted
    - Average Case: O(n^2)
    - Worst Case: O(n^2)

Space Complexity:
    - O(1)
"""

def insertion_sort(arr: list) -> list:
    for i in range(1, len(arr)):
        key = arr[i]
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

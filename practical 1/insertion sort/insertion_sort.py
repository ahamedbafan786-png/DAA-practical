"""
Time Complexity:
    - Best Case: O(n)
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
    user_input = input("Enter numbers separated by spaces: ")
    sample_data = list(map(int, user_input.split()))
    print("Original Array:", sample_data)
    sorted_data = insertion_sort(sample_data.copy())
    print("Sorted Array (Insertion Sort):", sorted_data)

"""
Time Complexity:
    - Best Case: O(n log n)
    - Average Case: O(n log n)
    - Worst Case: O(n log n)

Space Complexity:
    - O(n)
"""

def merge_sort(arr: list) -> list:
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr


if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces: ")
    sample_data = list(map(int, user_input.split()))
    print("Original Array:", sample_data)
    sorted_data = merge_sort(sample_data.copy())
    print("Sorted Array (Merge Sort):", sorted_data)
